# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntEnumConvert_test_convert_value_lookup_priority

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_type = enum.IntEnum._convert_('UnittestConvert', ('test.test_enum', '__main__')[__name__ == '__main__'], filter=lambda x: x.startswith('CONVERT_TEST_'))
    self.assertEqual(test_type(5).name, 'CONVERT_TEST_NAME_A')
