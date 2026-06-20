# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_int_literals_too_long

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    n = 3000
    source = f"a = 1\nb = 2\nc = {'3' * n}\nd = 4"
    with support.adjust_int_max_str_digits(n):
        compile(source, '<long_int_pass>', 'exec')
    with support.adjust_int_max_str_digits(n - 1):
        with self.assertRaises(SyntaxError) as err_ctx:
            compile(source, '<long_int_fail>', 'exec')
        exc = err_ctx.exception
        self.assertEqual(exc.lineno, 3)
        self.assertIn('Exceeds the limit ', str(exc))
        self.assertIn(' Consider hexadecimal ', str(exc))
