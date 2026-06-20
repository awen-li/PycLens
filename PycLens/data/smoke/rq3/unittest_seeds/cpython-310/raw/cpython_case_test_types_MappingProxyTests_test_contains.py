# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    view = self.mappingproxy(dict.fromkeys('abc'))
    self.assertTrue('a' in view)
    self.assertTrue('b' in view)
    self.assertTrue('c' in view)
    self.assertFalse('xxx' in view)
