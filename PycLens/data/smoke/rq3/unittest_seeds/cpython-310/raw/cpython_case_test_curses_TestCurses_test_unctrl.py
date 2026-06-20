# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_unctrl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(curses.unctrl(b'A'), b'A')
    self.assertEqual(curses.unctrl('A'), b'A')
    self.assertEqual(curses.unctrl(65), b'A')
    self.assertEqual(curses.unctrl(b'\n'), b'^J')
    self.assertEqual(curses.unctrl('\n'), b'^J')
    self.assertEqual(curses.unctrl(10), b'^J')
    self.assertRaises(TypeError, curses.unctrl, b'')
    self.assertRaises(TypeError, curses.unctrl, b'AB')
    self.assertRaises(TypeError, curses.unctrl, '')
    self.assertRaises(TypeError, curses.unctrl, 'AB')
    self.assertRaises(OverflowError, curses.unctrl, 2 ** 64)
