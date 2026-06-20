# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_conversions

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(f'{3.14:10.10}', '      3.14')
    self.assertEqual(f'{3.14!s:10.10}', '3.14      ')
    self.assertEqual(f'{3.14!r:10.10}', '3.14      ')
    self.assertEqual(f'{3.14!a:10.10}', '3.14      ')
    self.assertEqual(f"{'a'}", 'a')
    self.assertEqual(f"{'a'!r}", "'a'")
    self.assertEqual(f"{'a'!a}", "'a'")
    self.assertEqual(f"{'a!r'}", 'a!r')
    self.assertEqual(f'{3.14:!<10.10}', '3.14!!!!!!')
    self.assertAllRaise(SyntaxError, 'f-string: invalid conversion character', ["f'{3!g}'", "f'{3!A}'", "f'{3!3}'", "f'{3!G}'", "f'{3!!}'", "f'{3!:}'", "f'{3! s}'"])
    self.assertAllRaise(SyntaxError, "f-string: expecting '}'", ["f'{x!s{y}}'", "f'{3!ss}'", "f'{3!ss:}'", "f'{3!ss:s}'"])
