# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_inherited_data_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class HexInt(int):
        __qualname__ = 'HexInt'

        def __repr__(self):
            return hex(self)

    class MyEnum(HexInt, enum.Enum):
        __qualname__ = 'MyEnum'
        A = 1
        B = 2
        C = 3
    self.assertEqual(repr(MyEnum.A), '<MyEnum.A: 0x1>')
    globals()['HexInt'] = HexInt
    globals()['MyEnum'] = MyEnum
    test_pickle_dump_load(self.assertIs, MyEnum.A)
    test_pickle_dump_load(self.assertIs, MyEnum)

    class SillyInt(HexInt):
        __qualname__ = 'SillyInt'
        pass

    class MyOtherEnum(SillyInt, enum.Enum):
        __qualname__ = 'MyOtherEnum'
        D = 4
        E = 5
        F = 6
    self.assertIs(MyOtherEnum._member_type_, SillyInt)
    globals()['SillyInt'] = SillyInt
    globals()['MyOtherEnum'] = MyOtherEnum
    test_pickle_dump_load(self.assertIs, MyOtherEnum.E)
    test_pickle_dump_load(self.assertIs, MyOtherEnum)

    class BrokenInt(int):
        __qualname__ = 'BrokenInt'

        def __new__(cls, value):
            return int.__new__(cls, value)

    class MyBrokenEnum(BrokenInt, Enum):
        __qualname__ = 'MyBrokenEnum'
        G = 7
        H = 8
        I = 9
    self.assertIs(MyBrokenEnum._member_type_, BrokenInt)
    self.assertIs(MyBrokenEnum(7), MyBrokenEnum.G)
    globals()['BrokenInt'] = BrokenInt
    globals()['MyBrokenEnum'] = MyBrokenEnum
    test_pickle_exception(self.assertRaises, TypeError, MyBrokenEnum.G)
    test_pickle_exception(self.assertRaises, PicklingError, MyBrokenEnum)
