# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncgen.py
# case: AsyncGenAsyncioTest__check_async_iterator_anext_test_2

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g1 = ait_class()
    self.assertEqual(await anext(g1), 1)
    self.assertEqual(await anext(g1), 2)
    with self.assertRaises(StopAsyncIteration):
        await anext(g1)
    with self.assertRaises(StopAsyncIteration):
        await anext(g1)
    g2 = ait_class()
    self.assertEqual(await anext(g2, 'default'), 1)
    self.assertEqual(await anext(g2, 'default'), 2)
    self.assertEqual(await anext(g2, 'default'), 'default')
    self.assertEqual(await anext(g2, 'default'), 'default')
    return 'completed'
