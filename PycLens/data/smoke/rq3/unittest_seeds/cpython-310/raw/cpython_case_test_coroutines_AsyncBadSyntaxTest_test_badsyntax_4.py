# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_coroutines.py
# case: AsyncBadSyntaxTest_test_badsyntax_4

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    samples = ['def foo(await):\n                async def foo(): pass\n                async def foo():\n                    pass\n                return await + 1\n            ', 'def foo(await):\n                async def foo(): pass\n                async def foo(): pass\n                return await + 1\n            ', 'def foo(await):\n\n                async def foo(): pass\n\n                async def foo(): pass\n\n                return await + 1\n            ', 'def foo(await):\n                """spam"""\n                async def foo():                     pass\n                # 123\n                async def foo(): pass\n                # 456\n                return await + 1\n            ', 'def foo(await):\n                def foo(): pass\n                def foo(): pass\n                async def bar(): return await_\n                await_ = await\n                try:\n                    bar().send(None)\n                except StopIteration as ex:\n                    return ex.args[0] + 1\n            ']
    for code in samples:
        with self.subTest(code=code), self.assertRaises(SyntaxError):
            compile(code, '<test>', 'exec')
