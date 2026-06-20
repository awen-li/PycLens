# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pstats.py
# case: StatsTestCase_test_SortKey_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(SortKey.FILENAME, 'filename')
    self.assertNotEqual(SortKey.FILENAME, SortKey.CALLS)
