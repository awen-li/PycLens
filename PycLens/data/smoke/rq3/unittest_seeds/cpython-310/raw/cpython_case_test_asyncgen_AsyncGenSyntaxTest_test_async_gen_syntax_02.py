# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenSyntaxTest_test_async_gen_syntax_02

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = 'async def foo():\n            yield from 123\n        '
    with self.assertRaisesRegex(SyntaxError, 'yield from.*inside async'):
        exec(code, {}, {})
