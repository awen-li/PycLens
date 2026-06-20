# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: TestSSLDebug_test_keylog_env

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.addCleanup(os_helper.unlink, os_helper.TESTFN)
    with unittest.mock.patch.dict(os.environ):
        os.environ['SSLKEYLOGFILE'] = os_helper.TESTFN
        self.assertEqual(os.environ['SSLKEYLOGFILE'], os_helper.TESTFN)
        ctx = ssl.SSLContext(ssl.PROTOCOL_TLS_CLIENT)
        self.assertEqual(ctx.keylog_filename, None)
        ctx = ssl.create_default_context()
        self.assertEqual(ctx.keylog_filename, os_helper.TESTFN)
        ctx = ssl._create_stdlib_context()
        self.assertEqual(ctx.keylog_filename, os_helper.TESTFN)
