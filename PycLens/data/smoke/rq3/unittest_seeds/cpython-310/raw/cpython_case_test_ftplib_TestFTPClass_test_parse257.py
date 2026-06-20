# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_parse257

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(ftplib.parse257('257 "/foo/bar"'), '/foo/bar')
    self.assertEqual(ftplib.parse257('257 "/foo/bar" created'), '/foo/bar')
    self.assertEqual(ftplib.parse257('257 ""'), '')
    self.assertEqual(ftplib.parse257('257 "" created'), '')
    self.assertRaises(ftplib.error_reply, ftplib.parse257, '250 "/foo/bar"')
    self.assertEqual(ftplib.parse257('257 "/foo/b""ar"'), '/foo/b"ar')
    self.assertEqual(ftplib.parse257('257 "/foo/b""ar" created'), '/foo/b"ar')
