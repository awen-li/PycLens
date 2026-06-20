# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(take(10, cycle('abc')), list('abcabcabca'))
    self.assertEqual(list(cycle('')), [])
    self.assertRaises(TypeError, cycle)
    self.assertRaises(TypeError, cycle, 5)
    self.assertEqual(list(islice(cycle(gen3()), 10)), [0, 1, 2, 0, 1, 2, 0, 1, 2, 0])
