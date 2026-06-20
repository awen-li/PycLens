# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_resizeterm

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    curses.update_lines_cols()
    (lines, cols) = (curses.LINES, curses.COLS)
    new_lines = lines - 1
    new_cols = cols + 1
    curses.resizeterm(new_lines, new_cols)
    self.assertEqual(curses.LINES, new_lines)
    self.assertEqual(curses.COLS, new_cols)
    curses.resizeterm(lines, cols)
    self.assertEqual(curses.LINES, lines)
    self.assertEqual(curses.COLS, cols)
