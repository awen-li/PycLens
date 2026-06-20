# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: MappingProxyTests_test_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    attrs = set(dir(self.mappingproxy({}))) - set(dir(object()))
    self.assertEqual(attrs, {'__contains__', '__getitem__', '__class_getitem__', '__ior__', '__iter__', '__len__', '__or__', '__reversed__', '__ror__', 'copy', 'get', 'items', 'keys', 'values'})
