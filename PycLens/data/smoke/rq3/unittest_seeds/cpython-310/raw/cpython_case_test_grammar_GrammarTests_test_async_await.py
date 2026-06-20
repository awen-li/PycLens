# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_async_await

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    async def test():

        def sum():
            pass
        if 1:
            await someobj()
    self.assertEqual(test.__name__, 'test')
    self.assertTrue(bool(test.__code__.co_flags & inspect.CO_COROUTINE))

    def decorator(func):
        setattr(func, '_marked', True)
        return func

    @decorator
    async def test2():
        return 22
    self.assertTrue(test2._marked)
    self.assertEqual(test2.__name__, 'test2')
    self.assertTrue(bool(test2.__code__.co_flags & inspect.CO_COROUTINE))
