# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_out_of_complex_nested_blocks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output.append(1)
    for i in [1]:
        output.append(3)
        for j in [1, 2]:
            output.append(5)
            try:
                for k in [1, 2]:
                    output.append(8)
            finally:
                output.append(10)
        output.append(11)
    output.append(12)
