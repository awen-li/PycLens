# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_compile_top_level_await

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def arange(n):
        for i in range(n):
            yield i
    modes = ('single', 'exec')
    code_samples = ['a = await asyncio.sleep(0, result=1)', 'async for i in arange(1):\n                   a = 1', 'async with asyncio.Lock() as l:\n                   a = 1', 'a = [x async for x in arange(2)][1]', 'a = 1 in {x async for x in arange(2)}', 'a = {x:1 async for x in arange(1)}[0]', 'a = [x async for x in arange(2) async for x in arange(2)][1]', 'a = [x async for x in (x async for x in arange(5))][1]', 'a, = [1 for x in {x async for x in arange(1)}]', 'a = [await asyncio.sleep(0, x) async for x in arange(2)][1]']
    policy = maybe_get_event_loop_policy()
    try:
        for (mode, code_sample) in product(modes, code_samples):
            source = dedent(code_sample)
            with self.assertRaises(SyntaxError, msg=f'source={source} mode={mode}'):
                compile(source, '?', mode)
            co = compile(source, '?', mode, flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
            self.assertEqual(co.co_flags & CO_COROUTINE, CO_COROUTINE, msg=f'source={source} mode={mode}')
            globals_ = {'asyncio': asyncio, 'a': 0, 'arange': arange}
            async_f = FunctionType(co, globals_)
            asyncio.run(async_f())
            self.assertEqual(globals_['a'], 1)
            globals_ = {'asyncio': asyncio, 'a': 0, 'arange': arange}
            asyncio.run(eval(co, globals_))
            self.assertEqual(globals_['a'], 1)
    finally:
        asyncio.set_event_loop_policy(policy)
