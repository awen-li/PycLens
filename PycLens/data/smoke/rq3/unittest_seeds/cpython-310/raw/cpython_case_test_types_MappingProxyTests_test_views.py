# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_views

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mapping = {}
    view = self.mappingproxy(mapping)
    keys = view.keys()
    values = view.values()
    items = view.items()
    self.assertEqual(list(keys), [])
    self.assertEqual(list(values), [])
    self.assertEqual(list(items), [])
    mapping['key'] = 'value'
    self.assertEqual(list(keys), ['key'])
    self.assertEqual(list(values), ['value'])
    self.assertEqual(list(items), [('key', 'value')])
