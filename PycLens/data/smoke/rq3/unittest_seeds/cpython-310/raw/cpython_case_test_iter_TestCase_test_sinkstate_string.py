# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_iter.py
# case: TestCase_test_sinkstate_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = 'abcde'
    b = iter(a)
    self.assertEqual(list(b), ['a', 'b', 'c', 'd', 'e'])
    self.assertEqual(list(b), [])
