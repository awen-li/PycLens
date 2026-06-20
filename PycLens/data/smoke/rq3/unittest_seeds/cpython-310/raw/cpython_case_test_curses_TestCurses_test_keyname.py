# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_keyname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(curses.keyname(65), b'A')
    self.assertEqual(curses.keyname(13), b'^M')
    self.assertEqual(curses.keyname(127), b'^?')
    self.assertEqual(curses.keyname(0), b'^@')
    self.assertRaises(ValueError, curses.keyname, -1)
    self.assertIsInstance(curses.keyname(256), bytes)
