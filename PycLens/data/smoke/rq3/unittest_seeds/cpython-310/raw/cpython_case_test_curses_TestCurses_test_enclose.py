# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_enclose

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 2, 5)
    self.assertIs(win.enclose(2, 5), True)
    self.assertIs(win.enclose(1, 5), False)
    self.assertIs(win.enclose(2, 4), False)
    self.assertIs(win.enclose(6, 19), True)
    self.assertIs(win.enclose(7, 19), False)
    self.assertIs(win.enclose(6, 20), False)
