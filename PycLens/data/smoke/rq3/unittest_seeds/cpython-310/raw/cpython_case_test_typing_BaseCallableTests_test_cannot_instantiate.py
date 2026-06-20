# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_cannot_instantiate

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    with self.assertRaises(TypeError):
        Callable()
    with self.assertRaises(TypeError):
        type(Callable)()
    c = Callable[[int], str]
    with self.assertRaises(TypeError):
        c()
    with self.assertRaises(TypeError):
        type(c)()
