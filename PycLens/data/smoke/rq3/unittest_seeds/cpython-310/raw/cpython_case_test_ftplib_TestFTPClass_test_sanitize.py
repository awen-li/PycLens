# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_sanitize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.client.sanitize('foo'), repr('foo'))
    self.assertEqual(self.client.sanitize('pass 12345'), repr('pass *****'))
    self.assertEqual(self.client.sanitize('PASS 12345'), repr('PASS *****'))
