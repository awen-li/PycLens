# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_self_subclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    with self.assertRaises(TypeError):
        issubclass(types.FunctionType, Callable[[int], int])
    self.assertIsSubclass(types.FunctionType, Callable)
    self.assertIsSubclass(Callable, Callable)
