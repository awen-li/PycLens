# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ContextTests_test_check_hostname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with warnings_helper.check_warnings():
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS)
    self.assertFalse(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    ctx.check_hostname = True
    self.assertTrue(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_REQUIRED
    self.assertFalse(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_NONE
    ctx.check_hostname = False
    self.assertFalse(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
    ctx.check_hostname = True
    self.assertTrue(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_REQUIRED)
    ctx.check_hostname = False
    ctx.verify_mode = ssl.CERT_OPTIONAL
    ctx.check_hostname = False
    self.assertFalse(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_OPTIONAL)
    ctx.check_hostname = True
    self.assertTrue(ctx.check_hostname)
    self.assertEqual(ctx.verify_mode, ssl.CERT_OPTIONAL)
    with self.assertRaises(ValueError):
        ctx.verify_mode = ssl.CERT_NONE
    ctx.check_hostname = False
    self.assertFalse(ctx.check_hostname)
    ctx.verify_mode = ssl.CERT_NONE
    self.assertEqual(ctx.verify_mode, ssl.CERT_NONE)
