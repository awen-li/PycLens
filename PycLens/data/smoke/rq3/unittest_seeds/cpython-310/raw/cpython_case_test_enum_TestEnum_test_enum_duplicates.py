# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_enum_duplicates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Season(Enum):
        SPRING = 1
        SUMMER = 2
        AUTUMN = FALL = 3
        WINTER = 4
        ANOTHER_SPRING = 1
    lst = list(Season)
    self.assertEqual(lst, [Season.SPRING, Season.SUMMER, Season.AUTUMN, Season.WINTER])
    self.assertIs(Season.FALL, Season.AUTUMN)
    self.assertEqual(Season.FALL.value, 3)
    self.assertEqual(Season.AUTUMN.value, 3)
    self.assertIs(Season(3), Season.AUTUMN)
    self.assertIs(Season(1), Season.SPRING)
    self.assertEqual(Season.FALL.name, 'AUTUMN')
    self.assertEqual([k for (k, v) in Season.__members__.items() if v.name != k], ['FALL', 'ANOTHER_SPRING'])
