# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_get_default_verify_paths

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    paths = ssl.get_default_verify_paths()
    self.assertEqual(len(paths), 6)
    self.assertIsInstance(paths, ssl.DefaultVerifyPaths)
    with os_helper.EnvironmentVarGuard() as env:
        env['SSL_CERT_DIR'] = CAPATH
        env['SSL_CERT_FILE'] = CERTFILE
        paths = ssl.get_default_verify_paths()
        self.assertEqual(paths.cafile, CERTFILE)
        self.assertEqual(paths.capath, CAPATH)
