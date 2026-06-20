# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_union

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mapping = {'a': 0, 'b': 1, 'c': 2}
    view = self.mappingproxy(mapping)
    with self.assertRaises(TypeError):
        view | [('r', 2), ('d', 2)]
    with self.assertRaises(TypeError):
        [('r', 2), ('d', 2)] | view
    with self.assertRaises(TypeError):
        view |= [('r', 2), ('d', 2)]
    other = {'c': 3, 'p': 0}
    self.assertDictEqual(view | other, {'a': 0, 'b': 1, 'c': 3, 'p': 0})
    self.assertDictEqual(other | view, {'c': 2, 'p': 0, 'a': 0, 'b': 1})
    self.assertEqual(view, {'a': 0, 'b': 1, 'c': 2})
    self.assertDictEqual(mapping, {'a': 0, 'b': 1, 'c': 2})
    self.assertDictEqual(other, {'c': 3, 'p': 0})
