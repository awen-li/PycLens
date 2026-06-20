# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_read_oddinputs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._read_test([], [])
    self._read_test([''], [[]])
    self.assertRaises(csv.Error, self._read_test, ['"ab"c'], None, strict=1)
    self.assertRaises(csv.Error, self._read_test, ['ab\x00c'], None, strict=1)
    self._read_test(['"ab"c'], [['abc']], doublequote=0)
    self.assertRaises(csv.Error, self._read_test, [b'ab\x00c'], None)
