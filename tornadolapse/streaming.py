from io import BytesIO
from tornado.locks import Condition
from tornado.log import app_log


class StreamingOutput(object):
    last_frame = None
    frame = None
    buffer = BytesIO()
    condition = Condition()


class StreamingMJPEGOutput(StreamingOutput):

    name = "mjpeg"

    def __init__(self):
        self.frame = None
        self.buffer = BytesIO()
        self.condition = Condition()

    def write(self, buf):
        app_log.debug(f"Received {len(buf)} bytes of data")
        if buf.startswith(b'\xff\xd8'):
            # New frame, copy the existing buffer's content and notify all
            # clients it's available
            self.buffer.truncate()
            with self.condition:
                self.frame = self.buffer.getvalue()
                self.condition.notify_all()
            self.buffer.seek(0)
        return self.buffer.write(buf)

    def flush(self):
        app_log.debug("Received flush call")
        self.buffer.truncate()

        with self.condition:
            self.frame = self.buffer.getvalue()
            self.condition.notify_all()

        self.buffer.seek(0)