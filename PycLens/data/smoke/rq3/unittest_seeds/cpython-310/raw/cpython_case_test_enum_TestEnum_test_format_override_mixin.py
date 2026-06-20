# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_format_override_mixin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TestFloat(float, Enum):
        one = 1.0
        two = 2.0

        def __format__(self, spec):
            return 'TestFloat success!'
    self.assertEqual(str(TestFloat.one), 'TestFloat.one')
    self.assertEqual('{}'.format(TestFloat.one), 'TestFloat success!')
