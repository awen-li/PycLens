# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_deque.py
# case: TestBasic_test_copy_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mut = [10]
    d = deque([mut])
    e = d.copy()
    self.assertEqual(list(d), list(e))
    mut[0] = 11
    self.assertNotEqual(id(d), id(e))
    self.assertEqual(list(d), list(e))
