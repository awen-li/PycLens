# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: URL2PathNameTests_test_converting_drive_letter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(url2pathname('///C|'), 'C:')
    self.assertEqual(url2pathname('///C:'), 'C:')
    self.assertEqual(url2pathname('///C|/'), 'C:\\')
