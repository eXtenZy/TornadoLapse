#!/usr/bin/env python3.7
from tornado.ioloop import IOLoop
from tornado.options import options
from tornadolapse import TornadoLapse

if __name__ == "__main__":
    # Tornado configures logging.
    options.parse_command_line()
    app = TornadoLapse()
    app.listen(8080, max_body_size= 1024 * 1024 * 1024 * 10)
    IOLoop.current().start()
