# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_compile_async_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = dedent('async def ticker():\n                for i in range(10):\n                    yield i\n                    await asyncio.sleep(0)')
    co = compile(code, '?', 'exec', flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
    glob = {}
    exec(co, glob)
    self.assertEqual(type(glob['ticker']()), AsyncGeneratorType)
