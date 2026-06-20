# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_subclass_duplicate_name_dynamic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from types import DynamicClassAttribute

    class Base(Enum):

        @DynamicClassAttribute
        def test(self):
            return 'dynamic'

    class Test(Base):
        test = 1
    self.assertEqual(Test.test.test, 'dynamic')
