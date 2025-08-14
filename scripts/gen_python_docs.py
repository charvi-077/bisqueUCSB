#!/usr/bin/env python
# -*- coding: utf-8 -*-

import os
import ast
from pathlib import Path
from typing import List, Tuple

REPO_ROOT = Path('/workspace')
SRC_ROOT = REPO_ROOT / 'source'
OUTPUT_ROOT = REPO_ROOT / 'docs' / 'api' / 'python' / 'reference'

INCLUDE_DIRS = [
    SRC_ROOT / 'bqapi' / 'bqapi',
    SRC_ROOT / 'bqserver' / 'bq',
    SRC_ROOT / 'bqcore' / 'bq' / 'core',
    SRC_ROOT / 'bqengine' / 'bq' / 'engine',
    SRC_ROOT / 'bqfeature' / 'bq' / 'features',
]

EXCLUDE_PATTERNS = (
    '/tests/', '/test/', '/migrations/', '/public/', '/templates/'
)


def format_args(args: ast.arguments) -> str:
    names: List[str] = []
    # Positional args
    for a in args.args:
        names.append(a.arg)
    if args.vararg:
        names.append('*' + args.vararg.arg)
    # Keyword-only
    for a in getattr(args, 'kwonlyargs', []):
        names.append(a.arg)
    if args.kwarg:
        names.append('**' + args.kwarg.arg)
    # Remove self/cls from the start
    if names and names[0] in ('self', 'cls'):
        names = names[1:]
    return ', '.join(names)


def docstring(node: ast.AST) -> str:
    return (ast.get_docstring(node) or '').strip()


def collect_module(api_path: Path) -> Tuple[str, List[str]]:
    rel = api_path.relative_to(REPO_ROOT)
    module_title = f"## Module `{rel}`"
    with api_path.open('r', encoding='utf-8', errors='ignore') as f:
        src = f.read()
    try:
        tree = ast.parse(src)
    except SyntaxError:
        return module_title, []

    out: List[str] = []

    # Module docstring
    mdoc = docstring(tree)
    if mdoc:
        out.append(mdoc)
        out.append('')

    # Top-level functions
    funcs = [n for n in tree.body if isinstance(n, ast.FunctionDef) and not n.name.startswith('_')]
    if funcs:
        out.append('### Functions')
        out.append('')
        for fn in funcs:
            out.append(f"#### `{fn.name}({format_args(fn.args)})`")
            fdoc = docstring(fn)
            if fdoc:
                out.append('')
                out.append(fdoc)
            out.append('')

    # Classes
    classes = [n for n in tree.body if isinstance(n, ast.ClassDef) and not n.name.startswith('_')]
    if classes:
        out.append('### Classes')
        out.append('')
        for cls in classes:
            out.append(f"#### `{cls.name}`")
            cdoc = docstring(cls)
            if cdoc:
                out.append('')
                out.append(cdoc)
            out.append('')
            # Methods
            methods = [m for m in cls.body if isinstance(m, ast.FunctionDef) and not m.name.startswith('_')]
            if methods:
                out.append('Methods:')
                for m in methods:
                    out.append(f"- `{m.name}({format_args(m.args)})`")
                out.append('')
    return module_title, out


def should_skip(path: Path) -> bool:
    s = str(path)
    return any(p in s for p in EXCLUDE_PATTERNS)


def main() -> None:
    OUTPUT_ROOT.mkdir(parents=True, exist_ok=True)

    index_lines: List[str] = []
    index_lines.append('## Python Reference')
    index_lines.append('')

    for base in INCLUDE_DIRS:
        if not base.exists():
            continue
        for py in base.rglob('*.py'):
            if py.name.startswith('_'):
                continue
            if should_skip(py):
                continue
            title, body = collect_module(py)
            if not body:
                continue
            rel_md = (py.relative_to(SRC_ROOT)).with_suffix('.md')
            out_path = OUTPUT_ROOT / rel_md
            out_path.parent.mkdir(parents=True, exist_ok=True)
            with out_path.open('w', encoding='utf-8') as f:
                f.write(title + '\n\n')
                f.write('\n'.join(body))
            index_lines.append(f"- `{py.relative_to(SRC_ROOT)}` -> `docs/api/python/reference/{rel_md}`")

    with (OUTPUT_ROOT / 'README.md').open('w', encoding='utf-8') as f:
        f.write('\n'.join(index_lines))

if __name__ == '__main__':
    main()