# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_too_many_data_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaisesRegex(TypeError, 'too many data types'):

        class Huh(str, int, Enum):
            One = 1

    class MyStr(str):

        def hello(self):
            return 'hello, %s' % self

    class MyInt(int):

        def repr(self):
            return hex(self)
    with self.assertRaisesRegex(TypeError, 'too many data types'):

        class Huh(MyStr, MyInt, Enum):
            One = 1
