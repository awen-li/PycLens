# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_multiple_mixin_mro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class auto_enum(type(Enum)):

        def __new__(metacls, cls, bases, classdict):
            temp = type(classdict)()
            temp._cls_name = cls
            names = set(classdict._member_names)
            i = 0
            for k in classdict._member_names:
                v = classdict[k]
                if v is Ellipsis:
                    v = i
                else:
                    i = v
                i += 1
                temp[k] = v
            for (k, v) in classdict.items():
                if k not in names:
                    temp[k] = v
            return super(auto_enum, metacls).__new__(metacls, cls, bases, temp)

    class AutoNumberedEnum(Enum, metaclass=auto_enum):
        pass

    class AutoIntEnum(IntEnum, metaclass=auto_enum):
        pass

    class TestAutoNumber(AutoNumberedEnum):
        a = ...
        b = 3
        c = ...

    class TestAutoInt(AutoIntEnum):
        a = ...
        b = 3
        c = ...
