from tornado.web import Application
from tornado.ioloop import IOLoop, PeriodicCallback
from tornado.log import app_log
from tornado.options import options
from tornadolapse.handlers import StreamHandler


class TornadoLapse(Application):

    time_lapse_timer = None

    # List of request handlers
    handlers = list()

    debug = False

    io_loop = None

    camera = None

    def blink(self):
        app_log.info("Blink")


    def __init__(self):
        self.io_loop = IOLoop.current()
        if options.logging == 'debug':
            self.debug = True

        self.handlers.append((r"/(.*)", StreamHandler))
        Application.__init__(self, handlers=self.handlers, debug=self.debug, autoreload=self.debug,
                             static_path="filebrowser/static", template_path="filebrowser/templates")

        # Initialize camera

        self.io_loop.add_callback(self.init_camera)

    def init_camera(self):
        pass