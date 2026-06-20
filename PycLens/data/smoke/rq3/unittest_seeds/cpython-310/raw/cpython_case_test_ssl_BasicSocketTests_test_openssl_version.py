# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: BasicSocketTests_test_openssl_version

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = ssl.OPENSSL_VERSION_NUMBER
    t = ssl.OPENSSL_VERSION_INFO
    s = ssl.OPENSSL_VERSION
    self.assertIsInstance(n, int)
    self.assertIsInstance(t, tuple)
    self.assertIsInstance(s, str)
    self.assertGreaterEqual(n, 269488128)
    self.assertLess(n, 1073741824)
    (major, minor, fix, patch, status) = t
    self.assertGreaterEqual(major, 1)
    self.assertLess(major, 4)
    self.assertGreaterEqual(minor, 0)
    self.assertLess(minor, 256)
    self.assertGreaterEqual(fix, 0)
    self.assertLess(fix, 256)
    self.assertGreaterEqual(patch, 0)
    self.assertLessEqual(patch, 63)
    self.assertGreaterEqual(status, 0)
    self.assertLessEqual(status, 15)
    libressl_ver = f'LibreSSL {major:d}'
    if major >= 3:
        openssl_ver = f'OpenSSL {major:d}.{minor:d}.{patch:d}'
    else:
        openssl_ver = f'OpenSSL {major:d}.{minor:d}.{fix:d}'
    self.assertTrue(s.startswith((openssl_ver, libressl_ver)), (s, t, hex(n)))
