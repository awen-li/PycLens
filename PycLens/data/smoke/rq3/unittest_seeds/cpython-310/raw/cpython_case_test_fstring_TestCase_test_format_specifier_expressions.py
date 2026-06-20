# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_format_specifier_expressions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    width = 10
    precision = 4
    value = decimal.Decimal('12.34567')
    self.assertEqual(f'result: {value:{width}.{precision}}', 'result:      12.35')
    self.assertEqual(f'result: {value:{width!r}.{precision}}', 'result:      12.35')
    self.assertEqual(f'result: {value:{width:0}.{precision:1}}', 'result:      12.35')
    self.assertEqual(f'result: {value:{1}{0:0}.{precision:1}}', 'result:      12.35')
    self.assertEqual(f'result: {value:{1}{0:0}.{precision:1}}', 'result:      12.35')
    self.assertEqual(f'{10:#{1}0x}', '       0xa')
    self.assertEqual(f"{10:{'#'}1{0}{'x'}}", '       0xa')
    self.assertEqual(f"{-10:-{'#'}1{0}x}", '      -0xa')
    self.assertEqual(f"{-10:{'-'}#{1}0{'x'}}", '      -0xa')
    self.assertEqual(f'{10:#{3 != {4: 5} and width}x}', '       0xa')
    self.assertAllRaise(SyntaxError, "f-string: expecting '}'", ['f\'{"s"!r{":10"}}\''])
    self.assertAllRaise(SyntaxError, 'f-string: invalid syntax', ["f'{4:{/5}}'"])
    self.assertAllRaise(SyntaxError, 'f-string: expressions nested too deeply', ["f'result: {value:{width:{0}}.{precision:1}}'"])
    self.assertAllRaise(SyntaxError, 'f-string: invalid conversion character', ['f\'{"s"!{"r"}}\''])
