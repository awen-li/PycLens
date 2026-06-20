# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_pair_content

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not hasattr(curses, 'use_default_colors'):
        self.assertEqual(curses.pair_content(0), (curses.COLOR_WHITE, curses.COLOR_BLACK))
    curses.pair_content(0)
    maxpair = self.get_pair_limit() - 1
    if maxpair > 0:
        curses.pair_content(maxpair)
    for pair in self.bad_pairs():
        self.assertRaises(ValueError, curses.pair_content, pair)
