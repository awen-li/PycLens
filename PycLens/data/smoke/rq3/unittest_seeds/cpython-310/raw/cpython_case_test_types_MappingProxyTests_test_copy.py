# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_copy

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    original = {'key1': 27, 'key2': 51, 'key3': 93}
    view = self.mappingproxy(original)
    copy = view.copy()
    self.assertEqual(type(copy), dict)
    self.assertEqual(copy, original)
    original['key1'] = 70
    self.assertEqual(view['key1'], 70)
    self.assertEqual(copy['key1'], 27)
