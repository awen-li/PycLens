# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_no_jump_over_return_out_of_finally_block

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        output.append(2)
    finally:
        output.append(4)
        output.append(5)
        return
    output.append(7)
