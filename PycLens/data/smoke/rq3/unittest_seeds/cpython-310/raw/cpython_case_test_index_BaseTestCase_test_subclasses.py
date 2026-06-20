# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_index.py
# case: BaseTestCase_test_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = list(range(10))
    self.assertEqual(r[TrapInt(5):TrapInt(10)], r[5:10])
    self.assertEqual(slice(TrapInt()).indices(0), (0, 0, 1))
