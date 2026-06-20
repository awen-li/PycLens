# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_defaultdict.py
# case: TestDefaultDict_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = defaultdict()
    d2 = d1.copy()
    self.assertEqual(type(d2), defaultdict)
    self.assertEqual(d2.default_factory, None)
    self.assertEqual(d2, {})
    d1.default_factory = list
    d3 = d1.copy()
    self.assertEqual(type(d3), defaultdict)
    self.assertEqual(d3.default_factory, list)
    self.assertEqual(d3, {})
    d1[42]
    d4 = d1.copy()
    self.assertEqual(type(d4), defaultdict)
    self.assertEqual(d4.default_factory, list)
    self.assertEqual(d4, {42: []})
    d4[12]
    self.assertEqual(d4, {42: [], 12: []})
    d = defaultdict()
    d['a'] = 42
    e = d.copy()
    self.assertEqual(e['a'], 42)
