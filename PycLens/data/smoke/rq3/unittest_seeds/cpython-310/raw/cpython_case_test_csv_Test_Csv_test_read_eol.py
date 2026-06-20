# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_csv.py
# case: Test_Csv_test_read_eol

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self._read_test(['a,b'], [['a', 'b']])
    self._read_test(['a,b\n'], [['a', 'b']])
    self._read_test(['a,b\r\n'], [['a', 'b']])
    self._read_test(['a,b\r'], [['a', 'b']])
    self.assertRaises(csv.Error, self._read_test, ['a,b\rc,d'], [])
    self.assertRaises(csv.Error, self._read_test, ['a,b\nc,d'], [])
    self.assertRaises(csv.Error, self._read_test, ['a,b\r\nc,d'], [])
