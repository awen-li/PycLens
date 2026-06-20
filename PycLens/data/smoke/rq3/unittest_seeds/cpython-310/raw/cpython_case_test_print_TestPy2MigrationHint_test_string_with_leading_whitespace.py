# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_print.py
# case: TestPy2MigrationHint_test_string_with_leading_whitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    python2_print_str = 'if 1:\n            print "Hello World"\n        '
    with self.assertRaises(SyntaxError) as context:
        exec(python2_print_str)
    self.assertIn("Missing parentheses in call to 'print'. Did you mean print(...)", str(context.exception))
