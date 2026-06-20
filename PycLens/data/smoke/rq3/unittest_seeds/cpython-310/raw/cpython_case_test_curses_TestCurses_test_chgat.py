# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_chgat

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 5, 2)
    win.addstr(2, 0, 'Lorem ipsum')
    win.addstr(3, 0, 'dolor sit amet')
    win.move(2, 8)
    win.chgat(curses.A_BLINK)
    self.assertEqual(win.inch(2, 7), b'p'[0])
    self.assertEqual(win.inch(2, 8), b's'[0] | curses.A_BLINK)
    self.assertEqual(win.inch(2, 14), b' '[0] | curses.A_BLINK)
    win.move(2, 1)
    win.chgat(3, curses.A_BOLD)
    self.assertEqual(win.inch(2, 0), b'L'[0])
    self.assertEqual(win.inch(2, 1), b'o'[0] | curses.A_BOLD)
    self.assertEqual(win.inch(2, 3), b'e'[0] | curses.A_BOLD)
    self.assertEqual(win.inch(2, 4), b'm'[0])
    win.chgat(3, 2, curses.A_UNDERLINE)
    self.assertEqual(win.inch(3, 1), b'o'[0])
    self.assertEqual(win.inch(3, 2), b'l'[0] | curses.A_UNDERLINE)
    self.assertEqual(win.inch(3, 14), b' '[0] | curses.A_UNDERLINE)
    win.chgat(3, 4, 7, curses.A_BLINK)
    self.assertEqual(win.inch(3, 3), b'o'[0] | curses.A_UNDERLINE)
    self.assertEqual(win.inch(3, 4), b'r'[0] | curses.A_BLINK)
    self.assertEqual(win.inch(3, 10), b'a'[0] | curses.A_BLINK)
    self.assertEqual(win.inch(3, 11), b'm'[0] | curses.A_UNDERLINE)
    self.assertEqual(win.inch(3, 14), b' '[0] | curses.A_UNDERLINE)
