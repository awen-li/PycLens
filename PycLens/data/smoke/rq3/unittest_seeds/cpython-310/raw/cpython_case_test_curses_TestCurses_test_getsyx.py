# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_getsyx

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (y, x) = curses.getsyx()
    self.assertIsInstance(y, int)
    self.assertIsInstance(x, int)
    curses.setsyx(4, 5)
    self.assertEqual(curses.getsyx(), (4, 5))
