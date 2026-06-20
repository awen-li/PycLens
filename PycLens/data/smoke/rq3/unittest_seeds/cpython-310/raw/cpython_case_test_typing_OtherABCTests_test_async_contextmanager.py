# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: OtherABCTests_test_async_contextmanager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NotACM:
        pass
    self.assertIsInstance(ACM(), typing.AsyncContextManager)
    self.assertNotIsInstance(NotACM(), typing.AsyncContextManager)

    @contextlib.contextmanager
    def manager():
        yield 42
    cm = manager()
    self.assertNotIsInstance(cm, typing.AsyncContextManager)
    self.assertEqual(typing.AsyncContextManager[int].__args__, (int,))
    with self.assertRaises(TypeError):
        isinstance(42, typing.AsyncContextManager[int])
    with self.assertRaises(TypeError):
        typing.AsyncContextManager[int, str]
