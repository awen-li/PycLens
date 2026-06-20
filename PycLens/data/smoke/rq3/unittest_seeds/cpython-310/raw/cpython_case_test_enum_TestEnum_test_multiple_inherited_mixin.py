# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_multiple_inherited_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class StrEnum(str, Enum):

        def __new__(cls, *args, **kwargs):
            for a in args:
                if not isinstance(a, str):
                    raise TypeError("Enumeration '%s' (%s) is not a string" % (a, type(a).__name__))
            return str.__new__(cls, *args, **kwargs)

    @unique
    class Decision1(StrEnum):
        REVERT = 'REVERT'
        REVERT_ALL = 'REVERT_ALL'
        RETRY = 'RETRY'

    class MyEnum(StrEnum):
        pass

    @unique
    class Decision2(MyEnum):
        REVERT = 'REVERT'
        REVERT_ALL = 'REVERT_ALL'
        RETRY = 'RETRY'
