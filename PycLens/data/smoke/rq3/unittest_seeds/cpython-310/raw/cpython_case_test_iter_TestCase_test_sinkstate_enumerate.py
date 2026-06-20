# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_sinkstate_enumerate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = range(5)
    e = enumerate(a)
    b = iter(e)
    self.assertEqual(list(b), list(zip(range(5), range(5))))
    self.assertEqual(list(b), [])
