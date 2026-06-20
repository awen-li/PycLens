# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_reversed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d = {'a': 1, 'b': 2, 'foo': 0, 'c': 3, 'd': 4}
    mp = self.mappingproxy(d)
    del d['foo']
    r = reversed(mp)
    self.assertEqual(list(r), list('dcba'))
    self.assertRaises(StopIteration, next, r)
