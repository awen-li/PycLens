# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: TokenTests_test_end_of_numerical_literals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(test, error=False):
        with self.subTest(expr=test):
            if error:
                with warnings.catch_warnings(record=True) as w:
                    with self.assertRaises(SyntaxError):
                        compile(test, '<testcase>', 'eval')
                self.assertEqual(w, [])
            else:
                with self.assertWarns(DeprecationWarning):
                    compile(test, '<testcase>', 'eval')
    for num in ('0xf', '0o7', '0b1', '9', '0', '1.', '1e3', '1j'):
        compile(num, '<testcase>', 'eval')
        check(f'{num}and x', error=num == '0xf')
        check(f'{num}or x', error=num == '0')
        check(f'{num}in x')
        check(f'{num}not in x')
        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', '"is" with a literal', SyntaxWarning)
            check(f'{num}is x')
        check(f'{num}if x else y')
        check(f'x if {num}else y', error=num == '0xf')
        check(f'[{num}for x in ()]')
        check(f'{num}spam', error=True)
    check('[0x1ffor x in ()]')
    check('[0x1for x in ()]')
    check('[0xfor x in ()]')
