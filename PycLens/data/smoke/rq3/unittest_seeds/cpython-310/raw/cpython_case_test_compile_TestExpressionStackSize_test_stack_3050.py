# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestExpressionStackSize_test_stack_3050

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    M = 3050
    code = 'x,' * M + '=t'
    compile(code, '<foo>', 'single')
