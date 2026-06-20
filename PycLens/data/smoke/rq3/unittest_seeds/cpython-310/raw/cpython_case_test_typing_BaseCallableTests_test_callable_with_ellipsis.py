# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: BaseCallableTests_test_callable_with_ellipsis

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Callable = self.Callable

    def foo(a: Callable[..., T]):
        pass
    self.assertEqual(get_type_hints(foo, globals(), locals()), {'a': Callable[..., T]})
