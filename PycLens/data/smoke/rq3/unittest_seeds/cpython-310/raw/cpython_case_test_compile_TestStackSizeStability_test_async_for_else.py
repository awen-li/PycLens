# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestStackSizeStability_test_async_for_else

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snippet = '\n            async for x in y:\n                a\n            else:\n                b\n            '
    self.check_stack_size(snippet, async_=True)
