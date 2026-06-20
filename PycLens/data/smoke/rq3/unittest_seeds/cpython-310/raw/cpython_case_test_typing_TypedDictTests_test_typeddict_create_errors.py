# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_typeddict_create_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(TypeError):
        TypedDict.__new__()
    with self.assertRaises(TypeError):
        TypedDict()
    with self.assertRaises(TypeError):
        TypedDict('Emp', [('name', str)], None)
    with self.assertRaises(TypeError):
        TypedDict(_typename='Emp', name=str, id=int)
    with self.assertRaises(TypeError):
        TypedDict('Emp', _fields={'name': str, 'id': int})
