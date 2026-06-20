# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_enum_str_override

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyStrEnum(Enum):

        def __str__(self):
            return 'MyStr'

    class MyMethodEnum(Enum):

        def hello(self):
            return 'Hello!  My name is %s' % self.name

    class Test1Enum(MyMethodEnum, int, MyStrEnum):
        One = 1
        Two = 2
    self.assertTrue(Test1Enum._member_type_ is int)
    self.assertEqual(str(Test1Enum.One), 'MyStr')
    self.assertEqual(format(Test1Enum.One, ''), 'MyStr')

    class Test2Enum(MyStrEnum, MyMethodEnum):
        One = 1
        Two = 2
    self.assertEqual(str(Test2Enum.One), 'MyStr')
    self.assertEqual(format(Test1Enum.One, ''), 'MyStr')
