# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib_async.py
# case: AclosingTestCase_test_aclosing_bpo41229

async def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    state = []

    @contextmanager
    def sync_resource():
        try:
            yield
        finally:
            state.append(1)

    async def agenfunc():
        with sync_resource():
            yield (-1)
            yield (-2)
    x = agenfunc()
    self.assertEqual(state, [])
    with self.assertRaises(ZeroDivisionError):
        async with aclosing(x) as y:
            self.assertEqual(x, y)
            self.assertEqual(-1, await x.__anext__())
            1 / 0
    self.assertEqual(state, [1])
