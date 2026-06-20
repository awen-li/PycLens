# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_deep_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = defaultdict(foobar, {1: [1]})
    d2 = copy.deepcopy(d1)
    self.assertEqual(d2.default_factory, foobar)
    self.assertEqual(d2, d1)
    self.assertTrue(d1[1] is not d2[1])
    d1.default_factory = list
    d2 = copy.deepcopy(d1)
    self.assertEqual(d2.default_factory, list)
    self.assertEqual(d2, d1)
