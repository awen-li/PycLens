# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_read_from_window

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    stdscr.addstr(0, 1, 'ABCD', curses.A_BOLD)
    stdscr.move(0, 1)
    self.assertEqual(stdscr.inch(), 65 | curses.A_BOLD)
    self.assertEqual(stdscr.inch(0, 3), 67 | curses.A_BOLD)
    stdscr.move(0, 0)
    self.assertEqual(stdscr.instr()[:6], b' ABCD ')
    self.assertEqual(stdscr.instr(3)[:6], b' AB')
    self.assertEqual(stdscr.instr(0, 2)[:4], b'BCD ')
    self.assertEqual(stdscr.instr(0, 2, 4), b'BCD ')
    self.assertRaises(ValueError, stdscr.instr, -2)
    self.assertRaises(ValueError, stdscr.instr, 0, 2, -2)
