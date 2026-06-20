# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_ungetch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    curses.ungetch(b'A')
    self.assertEqual(self.stdscr.getkey(), 'A')
    curses.ungetch('B')
    self.assertEqual(self.stdscr.getkey(), 'B')
    curses.ungetch(67)
    self.assertEqual(self.stdscr.getkey(), 'C')
