# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_inherited_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyEnum(Enum):

        def __repr__(self):
            return 'My name is %s.' % self.name

    class MyIntEnum(int, MyEnum):
        this = 1
        that = 2
        theother = 3
    self.assertEqual(repr(MyIntEnum.that), 'My name is that.')
