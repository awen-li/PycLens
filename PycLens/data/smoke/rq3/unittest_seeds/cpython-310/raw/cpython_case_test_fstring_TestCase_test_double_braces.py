# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_double_braces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(f'{{', '{')
    self.assertEqual(f'a{{', 'a{')
    self.assertEqual(f'{{b', '{b')
    self.assertEqual(f'a{{b', 'a{b')
    self.assertEqual(f'}}', '}')
    self.assertEqual(f'a}}', 'a}')
    self.assertEqual(f'}}b', '}b')
    self.assertEqual(f'a}}b', 'a}b')
    self.assertEqual(f'{{}}', '{}')
    self.assertEqual(f'a{{}}', 'a{}')
    self.assertEqual(f'{{b}}', '{b}')
    self.assertEqual(f'{{}}c', '{}c')
    self.assertEqual(f'a{{b}}', 'a{b}')
    self.assertEqual(f'a{{}}c', 'a{}c')
    self.assertEqual(f'{{b}}c', '{b}c')
    self.assertEqual(f'a{{b}}c', 'a{b}c')
    self.assertEqual(f'{{{10}', '{10')
    self.assertEqual(f'}}{10}', '}10')
    self.assertEqual(f'}}{{{10}', '}{10')
    self.assertEqual(f'}}a{{{10}', '}a{10')
    self.assertEqual(f'{10}{{', '10{')
    self.assertEqual(f'{10}}}', '10}')
    self.assertEqual(f'{10}}}{{', '10}{')
    self.assertEqual(f'{10}}}a{{}}', '10}a{}')
    self.assertEqual(f"{'{{}}'}", '{{}}')
    self.assertAllRaise(TypeError, 'unhashable type', ["f'{ {{}} }'"])
