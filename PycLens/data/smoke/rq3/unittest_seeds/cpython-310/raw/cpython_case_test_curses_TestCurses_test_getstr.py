# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_getstr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 12, 5, 2)
    curses.echo()
    self.addCleanup(curses.noecho)
    self.assertRaises(ValueError, win.getstr, -400)
    self.assertRaises(ValueError, win.getstr, 2, 3, -400)
    for c in 'Lorem\nipsum\ndolor\nsit\namet\n'[::-1]:
        curses.ungetch(c)
    self.assertEqual(win.getstr(3, 1, 2), b'Lo')
    self.assertEqual(win.instr(3, 0), b' Lo         ')
    self.assertEqual(win.getstr(3, 5, 10), b'ipsum')
    self.assertEqual(win.instr(3, 0), b' Lo  ipsum  ')
    self.assertEqual(win.getstr(1, 5), b'dolor')
    self.assertEqual(win.instr(1, 0), b'     dolor  ')
    self.assertEqual(win.getstr(2), b'si')
    self.assertEqual(win.instr(1, 0), b'si   dolor  ')
    self.assertEqual(win.getstr(), b'amet')
    self.assertEqual(win.instr(1, 0), b'amet dolor  ')
