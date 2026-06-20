# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_context_custom_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MySSLSocket(ssl.SSLSocket):
        pass

    class MySSLObject(ssl.SSLObject):
        pass
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    ctx.sslsocket_class = MySSLSocket
    ctx.sslobject_class = MySSLObject
    with ctx.wrap_socket(socket.socket(), server_side=True) as sock:
        self.assertIsInstance(sock, MySSLSocket)
    obj = ctx.wrap_bio(ssl.MemoryBIO(), ssl.MemoryBIO(), server_side=True)
    self.assertIsInstance(obj, MySSLObject)
