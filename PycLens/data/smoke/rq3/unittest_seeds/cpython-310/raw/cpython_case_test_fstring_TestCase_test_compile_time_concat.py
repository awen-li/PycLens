# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_compile_time_concat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 'def'
    self.assertEqual(f'abc## {x}ghi', 'abc## defghi')
    self.assertEqual(f'abc{x}ghi', 'abcdefghi')
    self.assertEqual(f'abc{x}ghi{x:4}', 'abcdefghidef ')
    self.assertEqual(f'{{x}}{x}', '{x}def')
    self.assertEqual(f'{{x{x}', '{xdef')
    self.assertEqual(f'{{x}}{x}', '{x}def')
    self.assertEqual(f'{{{{x}}}}{x}', '{{x}}def')
    self.assertEqual(f'{{{{x{x}', '{{xdef')
    self.assertEqual(f'x}}}}{x}', 'x}}def')
    self.assertEqual(f'{x}x}}}}', 'defx}}')
    self.assertEqual(f'{x}', 'def')
    self.assertEqual(f'{x}', 'def')
    self.assertEqual(f'{x}', 'def')
    self.assertEqual(f'{x}2', 'def2')
    self.assertEqual(f'1{x}2', '1def2')
    self.assertEqual(f'1{x}', '1def')
    self.assertEqual(f'{x}-{x}', 'def-def')
    self.assertEqual(f'', '')
    self.assertEqual(f'', '')
    self.assertEqual(f'', '')
    self.assertEqual(f'', '')
    self.assertEqual(f'', '')
    self.assertEqual(f'', '')
    self.assertEqual(f'', '')
    self.assertAllRaise(SyntaxError, "f-string: expecting '}'", ["f'{3' f'}'"])
