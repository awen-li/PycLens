# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: CoroutineTests_test_non_gen_values

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @types.coroutine
    def foo():
        return 'spam'
    self.assertEqual(foo(), 'spam')

    class Awaitable:

        def __await__(self):
            return ()
    aw = Awaitable()

    @types.coroutine
    def foo():
        return aw
    self.assertIs(aw, foo())
    foo = types.coroutine(foo)
    self.assertIs(aw, foo())
