# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenTest_test_async_gen_api_01

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def gen():
        yield 123
    g = gen()
    self.assertEqual(g.__name__, 'gen')
    g.__name__ = '123'
    self.assertEqual(g.__name__, '123')
    self.assertIn('.gen', g.__qualname__)
    g.__qualname__ = '123'
    self.assertEqual(g.__qualname__, '123')
    self.assertIsNone(g.ag_await)
    self.assertIsInstance(g.ag_frame, types.FrameType)
    self.assertFalse(g.ag_running)
    self.assertIsInstance(g.ag_code, types.CodeType)
    self.assertTrue(inspect.isawaitable(g.aclose()))
