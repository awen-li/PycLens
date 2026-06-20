# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_attributes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 5, 2)
    win.attron(curses.A_BOLD)
    win.attroff(curses.A_BOLD)
    win.attrset(curses.A_BOLD)
    win.standout()
    win.standend()
