# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_global_param_err_first

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source = 'if 1:\n            def error(a):\n                global a  # SyntaxError\n            def error2():\n                b = 1\n                global b  # SyntaxError\n            '
    self._check_error(source, 'parameter and global', lineno=3)
