# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: GenericTests_test_init_subclass_super_called

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class FinalException(Exception):
        pass

    class Final:

        def __init_subclass__(cls, **kwargs) -> None:
            for base in cls.__bases__:
                if base is not Final and issubclass(base, Final):
                    raise FinalException(base)
            super().__init_subclass__(**kwargs)

    class Test(Generic[T], Final):
        pass
    with self.assertRaises(FinalException):

        class Subclass(Test):
            pass
    with self.assertRaises(FinalException):

        class Subclass(Test[int]):
            pass
