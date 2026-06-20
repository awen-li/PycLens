# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_backward_over_async_listcomp_v2

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    flag = False
    output.append(2)
    if flag:
        return
    x = [i async for i in asynciter(range(5))]
    flag = 6
    output.append(7)
    output.append(8)
