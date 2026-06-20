# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable
    alias = Callable[[int, str], float]
    if Callable is collections.abc.Callable:
        self.assertIsInstance(alias, types.GenericAlias)
    self.assertIs(alias.__origin__, collections.abc.Callable)
    self.assertEqual(alias.__args__, (int, str, float))
    self.assertEqual(alias.__parameters__, ())
