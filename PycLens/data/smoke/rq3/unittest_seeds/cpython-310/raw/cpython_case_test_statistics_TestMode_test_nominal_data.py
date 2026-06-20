# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: TestMode_test_nominal_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = 'abcbdb'
    self.assertEqual(self.func(data), 'b')
    data = 'fe fi fo fum fi fi'.split()
    self.assertEqual(self.func(data), 'fi')
