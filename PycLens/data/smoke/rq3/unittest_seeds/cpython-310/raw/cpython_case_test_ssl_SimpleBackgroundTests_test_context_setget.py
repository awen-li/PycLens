# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SimpleBackgroundTests_test_context_setget

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx1 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx1.load_verify_locations(capath=CAPATH)
    ctx2 = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    ctx2.load_verify_locations(capath=CAPATH)
    s = socket.socket(socket.AF_INET)
    with ctx1.wrap_socket(s, server_hostname='localhost') as ss:
        ss.connect(self.server_addr)
        self.assertIs(ss.context, ctx1)
        self.assertIs(ss._sslobj.context, ctx1)
        ss.context = ctx2
        self.assertIs(ss.context, ctx2)
        self.assertIs(ss._sslobj.context, ctx2)
