# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ConstantTests_test_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    nested_tuple = (1,)
    nested_frozenset = frozenset({1})
    for level in range(3):
        nested_tuple = (nested_tuple, 2)
        nested_frozenset = frozenset({nested_frozenset, 2})
    values = (123, 123.0, 123j, 'unicode', b'bytes', tuple('tuple'), frozenset('frozenset'), nested_tuple, nested_frozenset)
    for value in values:
        with self.subTest(value=value):
            result = self.compile_constant(value)
            self.assertEqual(result, value)
