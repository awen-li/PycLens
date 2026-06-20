# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: CollectionsAbcTests_test_coroutine

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {}
    exec('async def foo():\n    return\n', globals(), ns)
    foo = ns['foo']
    g = foo()
    self.assertIsInstance(g, typing.Coroutine)
    with self.assertRaises(TypeError):
        isinstance(g, typing.Coroutine[int])
    self.assertNotIsInstance(foo, typing.Coroutine)
    try:
        g.send(None)
    except StopIteration:
        pass
