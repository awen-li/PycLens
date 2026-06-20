# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_subclass_duplicate_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Base(Enum):

        def test(self):
            pass

    class Test(Base):
        test = 1
    self.assertIs(type(Test.test), Test)
