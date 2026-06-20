# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestStackSizeStability_test_for_break_continue_inside_async_with_block

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    snippet = '\n            for x in y:\n                async with c:\n                    if z:\n                        break\n                    elif u:\n                        continue\n                    else:\n                        a\n            else:\n                b\n            '
    self.check_stack_size(snippet, async_=True)
