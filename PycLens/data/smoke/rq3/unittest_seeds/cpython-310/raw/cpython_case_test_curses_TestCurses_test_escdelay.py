# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_escdelay

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    escdelay = curses.get_escdelay()
    self.assertIsInstance(escdelay, int)
    curses.set_escdelay(25)
    self.assertEqual(curses.get_escdelay(), 25)
    curses.set_escdelay(escdelay)
