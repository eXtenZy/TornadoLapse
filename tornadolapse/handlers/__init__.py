from tornado.web import RequestHandler


class StreamHandler(RequestHandler):
    def get(self, args) -> None:
        self.finish("What are youlooking at?")
