# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_strftime.py
# case: Y1900Tests_test_y_1900

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(time.strftime('%y', (1900, 1, 1, 0, 0, 0, 0, 0, 0)), '00')
