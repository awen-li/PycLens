# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_list.py
# case: ListTest_test_step_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = [0, 1, 2, 3, 4]
    a[1::sys.maxsize] = [0]
    self.assertEqual(a[3::sys.maxsize], [3])
