# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SSLErrorTests_test_lib_reason

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    with self.assertRaises(ssl.SSLError) as cm:
        ctx.load_dh_params(CERTFILE)
    self.assertEqual(cm.exception.library, 'PEM')
    self.assertEqual(cm.exception.reason, 'NO_START_LINE')
    s = str(cm.exception)
    self.assertTrue(s.startswith('[PEM: NO_START_LINE] no start line'), s)
