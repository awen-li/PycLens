# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_putwin

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 12, 1, 2)
    win.addstr(2, 1, 'Lorem ipsum')
    with tempfile.TemporaryFile() as f:
        win.putwin(f)
        del win
        f.seek(0)
        win = curses.getwin(f)
        self.assertEqual(win.getbegyx(), (1, 2))
        self.assertEqual(win.getmaxyx(), (5, 12))
        self.assertEqual(win.instr(2, 0), b' Lorem ipsum')
