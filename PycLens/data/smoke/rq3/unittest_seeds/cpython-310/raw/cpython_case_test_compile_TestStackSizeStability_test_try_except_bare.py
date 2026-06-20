# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestStackSizeStability_test_try_except_bare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snippet = '\n            try:\n                a\n            except:\n                b\n            '
    self.check_stack_size(snippet)
