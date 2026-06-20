# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_callable_instance_type_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable

    def f():
        pass
    with self.assertRaises(TypeError):
        self.assertIsInstance(f, Callable[[], None])
    with self.assertRaises(TypeError):
        self.assertIsInstance(f, Callable[[], Any])
    with self.assertRaises(TypeError):
        self.assertNotIsInstance(None, Callable[[], None])
    with self.assertRaises(TypeError):
        self.assertNotIsInstance(None, Callable[[], Any])
