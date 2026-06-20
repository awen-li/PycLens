# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_forwards_into_while_block

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    i = 1
    output.append(2)
    while i <= 2:
        output.append(4)
        i += 1
