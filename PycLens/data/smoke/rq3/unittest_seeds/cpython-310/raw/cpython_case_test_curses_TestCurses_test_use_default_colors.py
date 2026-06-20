# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_use_default_colors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old = curses.pair_content(0)
    try:
        curses.use_default_colors()
    except curses.error:
        self.skipTest('cannot change color (use_default_colors() failed)')
    self.assertEqual(curses.pair_content(0), (-1, -1))
    self.assertIn(old, [(curses.COLOR_WHITE, curses.COLOR_BLACK), (-1, -1), (0, 0)])
