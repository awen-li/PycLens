# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_resize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 2, 5)
    win.resize(4, 20)
    self.assertEqual(win.getmaxyx(), (4, 20))
    win.resize(5, 15)
    self.assertEqual(win.getmaxyx(), (5, 15))
