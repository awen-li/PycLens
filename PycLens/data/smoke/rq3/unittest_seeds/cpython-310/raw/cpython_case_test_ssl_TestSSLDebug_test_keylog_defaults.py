# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestSSLDebug_test_keylog_defaults

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
    self.assertEqual(ctx.keylog_filename, None)
    self.assertFalse(os.path.isfile(os_helper.TESTFN))
    ctx.keylog_filename = os_helper.TESTFN
    self.assertEqual(ctx.keylog_filename, os_helper.TESTFN)
    self.assertTrue(os.path.isfile(os_helper.TESTFN))
    self.assertEqual(self.keylog_lines(), 1)
    ctx.keylog_filename = None
    self.assertEqual(ctx.keylog_filename, None)
    with self.assertRaises((IsADirectoryError, PermissionError)):
        ctx.keylog_filename = os.path.dirname(os.path.abspath(os_helper.TESTFN))
    with self.assertRaises(TypeError):
        ctx.keylog_filename = 1
