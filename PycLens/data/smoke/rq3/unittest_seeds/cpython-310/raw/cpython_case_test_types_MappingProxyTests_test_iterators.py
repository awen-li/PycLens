# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_iterators

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    keys = ('x', 'y')
    values = (1, 2)
    items = tuple(zip(keys, values))
    view = self.mappingproxy(dict(items))
    self.assertEqual(set(view), set(keys))
    self.assertEqual(set(view.keys()), set(keys))
    self.assertEqual(set(view.values()), set(values))
    self.assertEqual(set(view.items()), set(items))
