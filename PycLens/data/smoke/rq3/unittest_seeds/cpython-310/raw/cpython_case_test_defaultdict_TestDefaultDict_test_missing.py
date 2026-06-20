# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_missing

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = defaultdict()
    self.assertRaises(KeyError, d1.__missing__, 42)
    d1.default_factory = list
    self.assertEqual(d1.__missing__(42), [])
