# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_background

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 5, 2)
    win.addstr(0, 0, 'Lorem ipsum')
    self.assertIn(win.getbkgd(), (0, 32))
    win.bkgdset('_')
    self.assertEqual(win.getbkgd(), b'_'[0])
    win.bkgdset(b'#')
    self.assertEqual(win.getbkgd(), b'#'[0])
    win.bkgdset(65)
    self.assertEqual(win.getbkgd(), 65)
    win.bkgdset(0)
    self.assertEqual(win.getbkgd(), 32)
    win.bkgdset('#', curses.A_REVERSE)
    self.assertEqual(win.getbkgd(), b'#'[0] | curses.A_REVERSE)
    self.assertEqual(win.inch(0, 0), b'L'[0])
    self.assertEqual(win.inch(0, 5), b' '[0])
    win.bkgdset(0)
    win.bkgd('_')
    self.assertEqual(win.getbkgd(), b'_'[0])
    self.assertEqual(win.inch(0, 0), b'L'[0])
    self.assertEqual(win.inch(0, 5), b'_'[0])
    win.bkgd('#', curses.A_REVERSE)
    self.assertEqual(win.getbkgd(), b'#'[0] | curses.A_REVERSE)
    self.assertEqual(win.inch(0, 0), b'L'[0] | curses.A_REVERSE)
    self.assertEqual(win.inch(0, 5), b'#'[0] | curses.A_REVERSE)
