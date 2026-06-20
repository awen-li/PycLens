# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_issue13051

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 2, 5)
    box = curses.textpad.Textbox(win, insert_mode=True)
    (lines, cols) = win.getmaxyx()
    win.resize(lines - 2, cols - 2)
    box._insert_printable_char('a')
