# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_async_with

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Done(Exception):
        pass

    class manager:

        async def __aenter__(self):
            return (1, 2)

        async def __aexit__(self, *exc):
            return False

    async def foo():
        async with manager():
            pass
        async with manager() as x:
            pass
        async with manager() as (x, y):
            pass
        async with manager(), manager():
            pass
        async with manager() as x, manager() as y:
            pass
        async with manager() as x, manager():
            pass
        raise Done
    with self.assertRaises(Done):
        foo().send(None)
