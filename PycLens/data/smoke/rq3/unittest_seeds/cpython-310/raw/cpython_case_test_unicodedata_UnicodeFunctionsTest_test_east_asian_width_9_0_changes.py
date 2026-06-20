# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeFunctionsTest_test_east_asian_width_9_0_changes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(self.db.ucd_3_2_0.east_asian_width('⌚'), 'N')
    self.assertEqual(self.db.east_asian_width('⌚'), 'W')
