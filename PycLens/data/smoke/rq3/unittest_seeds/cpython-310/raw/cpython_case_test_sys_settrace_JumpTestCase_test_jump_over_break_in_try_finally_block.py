# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_over_break_in_try_finally_block

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output.append(1)
    while True:
        output.append(3)
        try:
            output.append(5)
            if not output:
                break
            output.append(8)
        finally:
            output.append(10)
        output.append(11)
        break
    output.append(13)
