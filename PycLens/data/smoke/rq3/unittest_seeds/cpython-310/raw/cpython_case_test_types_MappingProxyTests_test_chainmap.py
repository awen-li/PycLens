# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_chainmap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    d1 = {'x': 1}
    d2 = {'y': 2}
    mapping = collections.ChainMap(d1, d2)
    view = self.mappingproxy(mapping)
    self.assertTrue('x' in view)
    self.assertTrue('y' in view)
    self.assertFalse('z' in view)
    self.assertEqual(view['x'], 1)
    self.assertEqual(view['y'], 2)
    self.assertRaises(KeyError, view.__getitem__, 'z')
    self.assertEqual(tuple(sorted(view)), ('x', 'y'))
    self.assertEqual(len(view), 2)
    copy = view.copy()
    self.assertIsNot(copy, mapping)
    self.assertIsInstance(copy, collections.ChainMap)
    self.assertEqual(copy, mapping)
    self.assertEqual(view.get('x'), 1)
    self.assertEqual(view.get('y'), 2)
    self.assertIsNone(view.get('z'))
    self.assertEqual(tuple(sorted(view.items())), (('x', 1), ('y', 2)))
    self.assertEqual(tuple(sorted(view.keys())), ('x', 'y'))
    self.assertEqual(tuple(sorted(view.values())), (1, 2))
