#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import re
import ast
from pathlib import Path
from typing import List, Dict, Any, Optional

REPO_ROOT = Path('/workspace')
SRC_ROOT = REPO_ROOT / 'source'
SERVER_ROOT = SRC_ROOT / 'bqserver' / 'bq'
CONTROLLERS_GLOB = '**/controllers/*.py'
OUTPUT_ROOT = REPO_ROOT / 'docs' / 'api' / 'rest'

# Simple dataclasses without imports to keep script self-contained
class ExposedMethod:
    def __init__(self, name: str, args: List[str], content_type: Optional[str], decorators: List[str], doc: Optional[str]):
        self.name = name
        self.args = args
        self.content_type = content_type
        self.decorators = decorators
        self.doc = (doc or '').strip()

class ControllerDoc:
    def __init__(self, service: str, controller: str, module_path: str):
        self.service = service
        self.controller = controller
        self.module_path = module_path
        self.methods: List[ExposedMethod] = []

    @property
    def base_path(self) -> str:
        return f'/{self.service}/'


def extract_string(node: ast.AST) -> Optional[str]:
    if isinstance(node, ast.Str):
        return node.s
    if isinstance(node, ast.Constant) and isinstance(node.value, str):
        return node.value
    return None


def get_function_docstring(fn: ast.FunctionDef) -> Optional[str]:
    if not fn.body:
        return None
    first = fn.body[0]
    if isinstance(first, ast.Expr):
        return extract_string(first.value)
    return None


def parse_expose_decorator(dec: ast.AST) -> Dict[str, Any]:
    """Parse @expose(...) decorator to capture content_type and any hints."""
    info: Dict[str, Any] = {'name': 'expose', 'content_type': None, 'raw': ''}
    try:
        if isinstance(dec, ast.Call):
            # raw decorator text fallback
            info['raw'] = 'expose(...)'
            for kw in dec.keywords:
                if kw.arg == 'content_type':
                    info['content_type'] = extract_string(kw.value)
        elif isinstance(dec, ast.Name) and dec.id == 'expose':
            info['raw'] = 'expose'
    except Exception:
        pass
    return info


def is_expose_decorator(dec: ast.AST) -> bool:
    # Supports @expose or @tg.expose or from tg import expose
    if isinstance(dec, ast.Name) and dec.id == 'expose':
        return True
    if isinstance(dec, ast.Attribute) and dec.attr == 'expose':
        return True
    if isinstance(dec, ast.Call):
        func = dec.func
        if isinstance(func, ast.Name) and func.id == 'expose':
            return True
        if isinstance(func, ast.Attribute) and func.attr == 'expose':
            return True
    return False


def discover_controllers(py_path: Path) -> List[ControllerDoc]:
    rel = py_path.relative_to(SERVER_ROOT)
    parts = rel.parts
    # Expect path like <service>/controllers/<file>.py
    if len(parts) < 3:
        return []
    service = parts[0]

    with py_path.open('r', encoding='utf-8', errors='ignore') as f:
        src = f.read()

    try:
        tree = ast.parse(src)
    except SyntaxError:
        return []

    controller_docs: List[ControllerDoc] = []

    for node in tree.body:
        if isinstance(node, ast.ClassDef):
            # Find *Controller classes
            if not node.name.endswith('Controller'):
                continue
            ctrl = ControllerDoc(service=service, controller=node.name, module_path=str(py_path.relative_to(REPO_ROOT)))
            # Inspect methods
            for sub in node.body:
                if isinstance(sub, ast.FunctionDef):
                    # Only public methods
                    if sub.name.startswith('_'):
                        continue
                    # Check for @expose decorator
                    decorators_text: List[str] = []
                    content_type = None
                    has_expose = False
                    for dec in sub.decorator_list:
                        if is_expose_decorator(dec):
                            has_expose = True
                            info = parse_expose_decorator(dec)
                            decorators_text.append(info.get('raw') or 'expose')
                            if info.get('content_type'):
                                content_type = info['content_type']
                        else:
                            # generic decorator string (best effort)
                            if isinstance(dec, ast.Name):
                                decorators_text.append(dec.id)
                            elif isinstance(dec, ast.Attribute):
                                decorators_text.append(dec.attr)
                            elif isinstance(dec, ast.Call):
                                if isinstance(dec.func, ast.Name):
                                    decorators_text.append(dec.func.id + '(...)')
                                elif isinstance(dec.func, ast.Attribute):
                                    decorators_text.append(dec.func.attr + '(...)')
                    if not has_expose:
                        continue
                    # Collect arg names excluding self
                    arg_names = [a.arg for a in sub.args.args if a.arg != 'self']
                    doc = get_function_docstring(sub)
                    ctrl.methods.append(ExposedMethod(sub.name, arg_names, content_type, decorators_text, doc))
            if ctrl.methods:
                controller_docs.append(ctrl)

    return controller_docs


def make_curl_example(base: str, method: ExposedMethod) -> str:
    # Heuristic mapping based on function name
    fn = method.name.lower()
    params = []
    for a in method.args:
        params.append(f'<{a}>')
    path_part = ''
    if fn in ('get', 'delete', 'put'):
        # assume first arg is resource identifier if present
        if params:
            path_part = '/' + params[0]
    elif fn == 'index':
        path_part = ''
    elif fn == 'post':
        path_part = ''
    else:
        # treat as GET under subpath
        path_part = '/' + method.name
        if params:
            path_part += '/' + '/'.join(params)

    # Determine HTTP verb
    if fn == 'post':
        verb = 'POST'
    elif fn == 'put':
        verb = 'PUT'
    elif fn == 'delete':
        verb = 'DELETE'
    else:
        verb = 'GET'

    content_hdr = ''
    if method.content_type and verb in ('POST', 'PUT'):
        content_hdr = f" -H 'Content-Type: {method.content_type}'"
    accept_hdr = ''
    if method.content_type and verb == 'GET':
        accept_hdr = f" -H 'Accept: {method.content_type}'"

    data_part = ''
    if verb in ('POST', 'PUT'):
        data_part = " -d '<payload>'"

    return f"curl -u <user>:<pass> -X {verb}{accept_hdr}{content_hdr}{data_part} '<host>{base.rstrip('/')}{path_part}'"


def render_controller_doc(ctrl: ControllerDoc) -> str:
    lines: List[str] = []
    lines.append(f"### Controller: {ctrl.controller}")
    lines.append('')
    lines.append(f"- **module**: `{ctrl.module_path}`")
    lines.append(f"- **base path**: `{ctrl.base_path}`")
    lines.append('')
    for m in sorted(ctrl.methods, key=lambda x: x.name):
        lines.append(f"#### `{m.name}({', '.join(m.args)})`")
        if m.doc:
            lines.append('')
            lines.append(m.doc)
        lines.append('')
        if m.content_type:
            lines.append(f"- **content_type**: `{m.content_type}`")
        if m.decorators:
            lines.append(f"- **decorators**: {', '.join(f'`{d}`' for d in m.decorators)}")
        lines.append(f"- **example**:")
        lines.append('')
        lines.append('```bash')
        lines.append(make_curl_example(ctrl.base_path, m))
        lines.append('```')
        lines.append('')
    return '\n'.join(lines)


def render_service_doc(service: str, controllers: List[ControllerDoc]) -> str:
    lines: List[str] = []
    lines.append(f"## Service: {service}")
    lines.append('')
    lines.append(f"- **base path**: `/{service}/`")
    lines.append('')
    lines.append('> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.')
    lines.append('')
    for ctrl in sorted(controllers, key=lambda c: c.controller):
        lines.append(render_controller_doc(ctrl))
        lines.append('')
    return '\n'.join(lines)


def main() -> None:
    controller_index: Dict[str, List[ControllerDoc]] = {}
    for py_file in (SERVER_ROOT.glob(CONTROLLERS_GLOB)):
        if py_file.name.startswith('_'):
            continue
        docs = discover_controllers(py_file)
        for doc in docs:
            controller_index.setdefault(doc.service, []).append(doc)

    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    # Write per-service docs
    for service, ctrls in sorted(controller_index.items()):
        out = render_service_doc(service, ctrls)
        out_path = OUTPUT_ROOT / f'{service}.md'
        with out_path.open('w', encoding='utf-8') as f:
            f.write(out)
    # Write an index README
    toc_lines: List[str] = []
    toc_lines.append('## REST API Reference')
    toc_lines.append('')
    toc_lines.append('This section documents REST endpoints for each service under the BisQue server. Endpoints were extracted from controller `@expose` methods.')
    toc_lines.append('')
    for service in sorted(controller_index.keys()):
        toc_lines.append(f"- [`{service}`](./{service}.md)")
    with (OUTPUT_ROOT / 'README.md').open('w', encoding='utf-8') as f:
        f.write('\n'.join(toc_lines))

if __name__ == '__main__':
    main()