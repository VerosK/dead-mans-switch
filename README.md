# Dead man's switch

> [Dead man's switch][dms] is a switch that is designed to be activated if the human operator becomes incapacitated.  Originally applied to switches on a vehicle or machine.

This small applications listens on HTTP port, registers
connections from applications and logs the connections
to Redis with short TTL

Another application (or Icinga check) can watch for the connection logs.

## Warning

This is proof-of-concept for testing dead man's switch concept for
monitoring of remote Icinga nodes.

I would recommend using [consul checks][consulchecks] for anything more
serious.

## License

BSD 2-Clause, or CC-0

[dms]: https://en.wikipedia.org/wiki/Dead_man%27s_switch
[consulchecks]: https://www.consul.io/docs/agent/checks.html