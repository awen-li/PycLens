# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_complex_subclasses

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    T_co = TypeVar('T_co', covariant=True)

    class Base(Generic[T_co]):
        ...
    T = TypeVar('T')

    class Sub(Base, Generic[T]):
        ...
