# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_enum.py
# case: TestEnum_test_enum

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Season = self.Season
    lst = list(Season)
    self.assertEqual(len(lst), len(Season))
    self.assertEqual(len(Season), 4, Season)
    self.assertEqual([Season.SPRING, Season.SUMMER, Season.AUTUMN, Season.WINTER], lst)
    for (i, season) in enumerate('SPRING SUMMER AUTUMN WINTER'.split(), 1):
        e = Season(i)
        self.assertEqual(e, getattr(Season, season))
        self.assertEqual(e.value, i)
        self.assertNotEqual(e, i)
        self.assertEqual(e.name, season)
        self.assertIn(e, Season)
        self.assertIs(type(e), Season)
        self.assertIsInstance(e, Season)
        self.assertEqual(str(e), 'Season.' + season)
        self.assertEqual(repr(e), '<Season.{0}: {1}>'.format(season, i))
