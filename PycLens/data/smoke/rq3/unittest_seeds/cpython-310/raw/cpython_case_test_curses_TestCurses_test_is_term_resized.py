# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_is_term_resized

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (lines, cols) = (curses.LINES, curses.COLS)
    self.assertIs(curses.is_term_resized(lines, cols), False)
    self.assertIs(curses.is_term_resized(lines - 1, cols - 1), True)
