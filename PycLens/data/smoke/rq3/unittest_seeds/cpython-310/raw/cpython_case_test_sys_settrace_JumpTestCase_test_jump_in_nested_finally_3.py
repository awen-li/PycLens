# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_in_nested_finally_3

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        output.append(2)
        1 / 0
        return
    finally:
        output.append(6)
        try:
            output.append(8)
        finally:
            output.append(10)
        output.append(11)
    output.append(12)
