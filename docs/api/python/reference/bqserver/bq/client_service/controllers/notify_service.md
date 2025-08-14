## Module `source/bqserver/bq/client_service/controllers/notify_service.py`

SYNOPSIS
========


DESCRIPTION
===========

Services for the notifying users.

### Functions

#### `send_mail(sender_email, recipients_email, subject, body)`

Send an email with  info to the user.

#### `send_invite(sender_email, recipient_email, subject, body)`

Create a new user and send them an invitation
returns the new BQuser

#### `initialize(uri)`

Initialize the top level server for this microapp

### Classes

#### `NotifyServerController`

Methods:
- `index(**kw)`
- `email(recipients, subject, body)`
