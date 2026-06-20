# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestIntEnumConvert_test_convert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    test_type = enum.IntEnum._convert_('UnittestConvert', ('test.test_enum', '__main__')[__name__ == '__main__'], filter=lambda x: x.startswith('CONVERT_TEST_'))
    self.assertEqual(test_type.CONVERT_TEST_NAME_F, test_type.CONVERT_TEST_NAME_A)
    self.assertEqual(test_type.CONVERT_TEST_NAME_B, 5)
    self.assertEqual(test_type.CONVERT_TEST_NAME_C, 5)
    self.assertEqual(test_type.CONVERT_TEST_NAME_D, 5)
    self.assertEqual(test_type.CONVERT_TEST_NAME_E, 5)
    self.assertEqual([name for name in dir(test_type) if name[0:2] not in ('CO', '__')], [], msg='Names other than CONVERT_TEST_* found.')
