# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_syntax.py
# case: SyntaxTestCase_test_barry_as_flufl_with_syntax_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = '\ndef func1():\n    if a != b:\n        raise ValueError\n\ndef func2():\n    try\n        return 1\n    finally:\n        pass\n'
    self._check_error(code, "expected ':'")
