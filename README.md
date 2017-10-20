# damn
Databse Middleman for Litecord

This establishes a connection with Postgres and
provides an HTTP API so that `gateway` and `rest` can communicate with.

## Reason

Both `gateway` and `rest` connecting to the same Postgres instance
could give us problems, specially on code duplication since both
require a library to work with.
