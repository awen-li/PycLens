# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_beep

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if curses.tigetstr('bel') is not None or curses.tigetstr('flash') is not None:
        curses.beep()
    else:
        try:
            curses.beep()
        except curses.error:
            self.skipTest('beep() failed')
