# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_endwin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not self.isatty:
        self.skipTest('requires terminal')
    self.assertIs(curses.isendwin(), False)
    curses.endwin()
    self.assertIs(curses.isendwin(), True)
    curses.doupdate()
    self.assertIs(curses.isendwin(), False)
