# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_over_async_for_block_before_else

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    output.append(1)
    if not output:
        async for i in asynciter([3]):
            output.append(4)
    else:
        output.append(6)
        output.append(7)
    output.append(8)
