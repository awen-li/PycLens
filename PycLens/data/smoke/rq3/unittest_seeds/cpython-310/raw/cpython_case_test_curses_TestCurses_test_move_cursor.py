# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_move_cursor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    win = stdscr.subwin(10, 15, 2, 5)
    stdscr.move(1, 2)
    win.move(2, 4)
    self.assertEqual(stdscr.getyx(), (1, 2))
    self.assertEqual(win.getyx(), (2, 4))
    win.cursyncup()
    self.assertEqual(stdscr.getyx(), (4, 9))
