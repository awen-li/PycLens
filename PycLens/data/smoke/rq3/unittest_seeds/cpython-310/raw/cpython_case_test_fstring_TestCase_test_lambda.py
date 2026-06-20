# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_lambda

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 5
    self.assertEqual(f"{(lambda y: x * y)('8')!r}", "'88888'")
    self.assertEqual(f"{(lambda y: x * y)('8')!r:10}", "'88888'   ")
    self.assertEqual(f"{(lambda y: x * y)('8'):10}", '88888     ')
    self.assertAllRaise(SyntaxError, 'f-string: invalid syntax', ["f'{lambda x:x}'"])
