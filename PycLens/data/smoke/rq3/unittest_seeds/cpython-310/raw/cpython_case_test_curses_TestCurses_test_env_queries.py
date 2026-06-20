# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_env_queries

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(curses.termname(), bytes)
    self.assertIsInstance(curses.longname(), bytes)
    self.assertIsInstance(curses.baudrate(), int)
    self.assertIsInstance(curses.has_ic(), bool)
    self.assertIsInstance(curses.has_il(), bool)
    self.assertIsInstance(curses.termattrs(), int)
    c = curses.killchar()
    self.assertIsInstance(c, bytes)
    self.assertEqual(len(c), 1)
    c = curses.erasechar()
    self.assertIsInstance(c, bytes)
    self.assertEqual(len(c), 1)
