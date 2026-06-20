# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_continuation_bad_indentation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\\\nif x:\n    y = 1\n  \\\n  foo = 1\n        '
    self.assertRaises(IndentationError, exec, code)
