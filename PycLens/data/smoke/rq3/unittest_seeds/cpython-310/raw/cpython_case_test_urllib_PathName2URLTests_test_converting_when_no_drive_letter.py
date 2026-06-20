# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: PathName2URLTests_test_converting_when_no_drive_letter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(pathname2url('\\\\\\folder\\test\\'), '/////folder/test/')
    self.assertEqual(pathname2url('\\\\folder\\test\\'), '////folder/test/')
    self.assertEqual(pathname2url('\\folder\\test\\'), '/folder/test/')
