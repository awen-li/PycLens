# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_settrace.py
# case: JumpTestCase_test_no_jump_backwards_into_async_for_block

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    async for i in asynciter([1, 2]):
        output.append(2)
    output.append(3)
