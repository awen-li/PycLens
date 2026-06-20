# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: NamedTupleTests_test_annotation_usage_with_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    jelle = CoolEmployeeWithDefault('Jelle')
    self.assertIsInstance(jelle, CoolEmployeeWithDefault)
    self.assertIsInstance(jelle, tuple)
    self.assertEqual(jelle.name, 'Jelle')
    self.assertEqual(jelle.cool, 0)
    cooler_employee = CoolEmployeeWithDefault('Sjoerd', 1)
    self.assertEqual(cooler_employee.cool, 1)
    self.assertEqual(CoolEmployeeWithDefault.__name__, 'CoolEmployeeWithDefault')
    self.assertEqual(CoolEmployeeWithDefault._fields, ('name', 'cool'))
    self.assertEqual(CoolEmployeeWithDefault.__annotations__, dict(name=str, cool=int))
    self.assertEqual(CoolEmployeeWithDefault._field_defaults, dict(cool=0))
    with self.assertRaises(TypeError):

        class NonDefaultAfterDefault(NamedTuple):
            x: int = 3
            y: int
