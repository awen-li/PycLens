# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_hash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    dates = {}
    dates[Season.WINTER] = '1225'
    dates[Season.SPRING] = '0315'
    dates[Season.SUMMER] = '0704'
    dates[Season.AUTUMN] = '1031'
    self.assertEqual(dates[Season.AUTUMN], '1031')
