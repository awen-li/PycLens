# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AclosingTestCase_test_aclosing

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = []

    class C:

        async def aclose(self):
            state.append(1)
    x = C()
    self.assertEqual(state, [])
    async with aclosing(x) as y:
        self.assertEqual(x, y)
    self.assertEqual(state, [1])
