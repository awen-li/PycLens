# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: EndPositionTests_test_yield_await

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = dedent('\n            async def f():\n                yield x\n                await y\n        ').strip()
    fdef = ast.parse(s).body[0]
    self._check_content(s, fdef.body[0].value, 'yield x')
    self._check_content(s, fdef.body[1].value, 'await y')
