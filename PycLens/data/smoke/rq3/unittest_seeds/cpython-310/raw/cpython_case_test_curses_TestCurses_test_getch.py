# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_getch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 12, 5, 2)
    for c in 'spam\n'[::-1]:
        curses.ungetch(c)
    self.assertEqual(win.getch(3, 1), b's'[0])
    self.assertEqual(win.getyx(), (3, 1))
    self.assertEqual(win.getch(3, 4), b'p'[0])
    self.assertEqual(win.getyx(), (3, 4))
    self.assertEqual(win.getch(), b'a'[0])
    self.assertEqual(win.getyx(), (3, 4))
    self.assertEqual(win.getch(), b'm'[0])
    self.assertEqual(win.getch(), b'\n'[0])
