# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for protocol in PROTOCOLS:
        if has_tls_protocol(protocol):
            with warnings_helper.check_warnings():
                ctx = ssl.SSLContext(protocol)
            self.assertEqual(ctx.protocol, protocol)
    with warnings_helper.check_warnings():
        ctx = ssl.SSLContext()
    self.assertEqual(ctx.protocol, ssl.PROTOCOL_TLS)
    self.assertRaises(ValueError, ssl.SSLContext, -1)
    self.assertRaises(ValueError, ssl.SSLContext, 42)
