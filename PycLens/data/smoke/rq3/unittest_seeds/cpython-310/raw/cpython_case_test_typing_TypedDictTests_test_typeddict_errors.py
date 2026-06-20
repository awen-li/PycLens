# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypedDictTests_test_typeddict_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Emp = TypedDict('Emp', {'name': str, 'id': int})
    self.assertEqual(TypedDict.__module__, 'typing')
    jim = Emp(name='Jim', id=1)
    with self.assertRaises(TypeError):
        isinstance({}, Emp)
    with self.assertRaises(TypeError):
        isinstance(jim, Emp)
    with self.assertRaises(TypeError):
        issubclass(dict, Emp)
    with self.assertRaises(TypeError):
        TypedDict('Hi', x=1)
    with self.assertRaises(TypeError):
        TypedDict('Hi', [('x', int), ('y', 1)])
    with self.assertRaises(TypeError):
        TypedDict('Hi', [('x', int)], y=int)
