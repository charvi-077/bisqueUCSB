## Service: client_service

- **base path**: `/client_service/`

> The following endpoints are discovered from TurboGears `@expose` methods in controllers. They map to conventional REST methods: `index` (GET collection), `get` (GET item), `post` (POST collection), `put` (PUT item), `delete` (DELETE item). Other method names are exposed at `/<method>`.

### Controller: NotifyServerController

- **module**: `source/bqserver/bq/client_service/controllers/notify_service.py`
- **base path**: `/client_service/`

#### `email(recipients, subject, body)`

Send an email for logged in users



        POST application/text   ?subject=required&recipient=required[,required][&body]
             TEXT BODY
        POST applcation/xml   ?subject=required&recipient=required[,required][&body]
        <message>
           <subject>.. </subject>
           <recipient> .. </recipient>
           <body> .. </body>
        </message>

- **content_type**: `text/xml`
- **decorators**: `expose(...)`, `require(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/client_service/email/<recipients>/<subject>/<body>'
```

#### `index()`

- **content_type**: `text/xml`
- **decorators**: `expose(...)`
- **example**:

```bash
curl -u <user>:<pass> -X GET -H 'Accept: text/xml' '<host>/client_service'
```

