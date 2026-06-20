# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_jump_out_of_async_for_block_backwards

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in [1]:
        output.append(2)
        async for i in asynciter([1]):
            output.append(4)
            output.append(5)
        output.append(6)
