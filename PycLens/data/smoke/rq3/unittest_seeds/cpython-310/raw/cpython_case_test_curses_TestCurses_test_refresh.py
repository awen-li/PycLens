# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_refresh

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 2, 5)
    win.noutrefresh()
    win.redrawln(1, 2)
    win.redrawwin()
    win.refresh()
    curses.doupdate()
