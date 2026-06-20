# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_mismatched_braces

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAllRaise(SyntaxError, "f-string: single '}' is not allowed", ["f'{{}'", "f'{{}}}'", "f'}'", "f'x}'", "f'x}x'", "f'\\u007b}'", "f'{3:}>10}'", "f'{3:}}>10}'"])
    self.assertAllRaise(SyntaxError, "f-string: expecting '}'", ["f'{3:{{>10}'", "f'{3'", "f'{3!'", "f'{3:'", "f'{3!s'", "f'{3!s:'", "f'{3!s:3'", "f'x{'", "f'x{x'", "f'{x'", "f'{3:s'", "f'{{{'", "f'{{}}{'", "f'{'", "f'x{<'", "f'x{>'", "f'{i='"])
    self.assertEqual(f"{'{'}", '{')
    self.assertEqual(f"{'}'}", '}')
    self.assertEqual(f"{3:{'}'}>10}", '}}}}}}}}}3')
    self.assertEqual(f"{2:{'{'}>10}", '{{{{{{{{{2')
