# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: MiscTests_test_update_lines_cols

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    curses.update_lines_cols()
    (lines, cols) = (curses.LINES, curses.COLS)
    curses.LINES = curses.COLS = 0
    curses.update_lines_cols()
    self.assertEqual(curses.LINES, lines)
    self.assertEqual(curses.COLS, cols)
