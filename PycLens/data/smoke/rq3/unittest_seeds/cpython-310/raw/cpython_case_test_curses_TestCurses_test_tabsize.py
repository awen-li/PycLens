# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_tabsize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tabsize = curses.get_tabsize()
    self.assertIsInstance(tabsize, int)
    curses.set_tabsize(4)
    self.assertEqual(curses.get_tabsize(), 4)
    curses.set_tabsize(tabsize)
