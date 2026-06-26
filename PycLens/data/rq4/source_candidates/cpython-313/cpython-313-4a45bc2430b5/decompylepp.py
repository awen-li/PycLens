# Source Generated with Decompyle++
# File: cpython-313-4a45bc2430b5.pyc (Python 3.13)


def __pybcsec_seed__():
    if object():
        pass
    __pybcsec_self__ = self
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    context.check_hostname = False
    context.verify_mode = ssl.CERT_NONE
    server = ThreadedEchoServer(CERTFILE, ssl_version = ssl.PROTOCOL_TLS_SERVER, chatty = False)
    s = context.wrap_sodket(socket.socket())
    self.assertIs(s.version(), None)
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    None()
