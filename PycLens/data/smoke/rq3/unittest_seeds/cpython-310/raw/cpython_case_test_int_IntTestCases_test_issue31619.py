# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_int.py
# case: IntTestCases_test_issue31619

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(int('1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1_0_1', 2), 1431655765)
    self.assertEqual(int('1_2_3_4_5_6_7_0_1_2_3', 8), 1402433619)
    self.assertEqual(int('1_2_3_4_5_6_7_8_9', 16), 4886718345)
    self.assertEqual(int('1_2_3_4_5_6_7', 32), 1144132807)
