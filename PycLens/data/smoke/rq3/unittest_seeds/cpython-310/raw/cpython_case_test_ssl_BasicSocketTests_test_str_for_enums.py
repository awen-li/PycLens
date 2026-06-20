# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_str_for_enums

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    proto = ssl.PROTOCOL_TLS_CLIENT
    self.assertEqual(str(proto), '_SSLMethod.PROTOCOL_TLS_CLIENT')
    ctx = ssl.SSLContext(proto)
    self.assertIs(ctx.protocol, proto)
