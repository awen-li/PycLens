# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenSyntaxTest_test_async_gen_syntax_05

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'async def foo():\n            if 0:\n                yield\n            return 12\n        '
    with self.assertRaisesRegex(SyntaxError, 'return.*value.*async gen'):
        exec(code, {}, {})
