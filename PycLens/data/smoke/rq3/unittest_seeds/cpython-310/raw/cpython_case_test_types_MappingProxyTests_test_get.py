# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    view = self.mappingproxy({'a': 'A', 'b': 'B'})
    self.assertEqual(view['a'], 'A')
    self.assertEqual(view['b'], 'B')
    self.assertRaises(KeyError, view.__getitem__, 'xxx')
    self.assertEqual(view.get('a'), 'A')
    self.assertIsNone(view.get('xxx'))
    self.assertEqual(view.get('xxx', 42), 42)
