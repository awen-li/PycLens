# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: TypeTests_test_type_optional

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    A = Optional[Type[BaseException]]

    def foo(a: A) -> Optional[BaseException]:
        if a is None:
            return None
        else:
            return a()
    assert isinstance(foo(KeyboardInterrupt), KeyboardInterrupt)
    assert foo(None) is None
