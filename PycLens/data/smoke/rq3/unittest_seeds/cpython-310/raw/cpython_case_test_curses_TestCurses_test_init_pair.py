# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_init_pair

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old = curses.pair_content(1)
    curses.init_pair(1, *old)
    self.addCleanup(curses.init_pair, 1, *old)
    curses.init_pair(1, 0, 0)
    self.assertEqual(curses.pair_content(1), (0, 0))
    maxcolor = curses.COLORS - 1
    curses.init_pair(1, maxcolor, 0)
    self.assertEqual(curses.pair_content(1), (maxcolor, 0))
    curses.init_pair(1, 0, maxcolor)
    self.assertEqual(curses.pair_content(1), (0, maxcolor))
    maxpair = self.get_pair_limit() - 1
    if maxpair > 1:
        curses.init_pair(maxpair, 0, 0)
        self.assertEqual(curses.pair_content(maxpair), (0, 0))
    for pair in self.bad_pairs():
        self.assertRaises(ValueError, curses.init_pair, pair, 0, 0)
    for color in self.bad_colors2():
        self.assertRaises(ValueError, curses.init_pair, 1, color, 0)
        self.assertRaises(ValueError, curses.init_pair, 1, 0, color)
