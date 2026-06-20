# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_compile_top_level_await_invalid_cases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def arange(n):
        for i in range(n):
            yield i
    modes = ('single', 'exec')
    code_samples = ['def f():  await arange(10)\n', 'def f():  [x async for x in arange(10)]\n', 'def f():  [await x async for x in arange(10)]\n', 'def f():\n                   async for i in arange(1):\n                       a = 1\n            ', 'def f():\n                   async with asyncio.Lock() as l:\n                       a = 1\n            ']
    policy = maybe_get_event_loop_policy()
    try:
        for (mode, code_sample) in product(modes, code_samples):
            source = dedent(code_sample)
            with self.assertRaises(SyntaxError, msg=f'source={source} mode={mode}'):
                compile(source, '?', mode)
            with self.assertRaises(SyntaxError, msg=f'source={source} mode={mode}'):
                co = compile(source, '?', mode, flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    finally:
        asyncio.set_event_loop_policy(policy)
