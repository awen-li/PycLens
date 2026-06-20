# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_contains_tf

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    self.assertIn(Season.AUTUMN, Season)
    self.assertTrue(3 in Season)
    self.assertFalse('AUTUMN' in Season)
    val = Season(3)
    self.assertIn(val, Season)

    class OtherEnum(Enum):
        one = 1
        two = 2
    self.assertNotIn(OtherEnum.two, Season)
