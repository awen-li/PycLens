# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestStackSizeStability_test_try_except_qualified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snippet = '\n            try:\n                a\n            except ImportError:\n                b\n            except:\n                c\n            else:\n                d\n            '
    self.check_stack_size(snippet)
