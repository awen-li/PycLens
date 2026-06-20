# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_multiple_mixin_inherited

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyInt(int):

        def __new__(cls, value):
            return super().__new__(cls, value)

    class HexMixin:

        def __repr__(self):
            return hex(self)

    class MyIntEnum(HexMixin, MyInt, enum.Enum):
        pass

    class Foo(MyIntEnum):
        TEST = 1
    self.assertTrue(isinstance(Foo.TEST, MyInt))
    self.assertEqual(repr(Foo.TEST), '0x1')

    class Fee(MyIntEnum):
        TEST = 1

        def __new__(cls, value):
            value += 1
            member = int.__new__(cls, value)
            member._value_ = value
            return member
    self.assertEqual(Fee.TEST, 2)
