# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestStackSizeStability_test_if_else

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snippet = '\n            if x:\n                a\n            elif y:\n                b\n            else:\n                c\n            '
    self.check_stack_size(snippet)
