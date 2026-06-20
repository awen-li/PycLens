# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_clear

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 5, 2)
    lorem_ipsum(win)
    win.move(0, 8)
    win.clrtoeol()
    self.assertEqual(win.instr(0, 0).rstrip(), b'Lorem ip')
    self.assertEqual(win.instr(1, 0).rstrip(), b'dolor sit amet,')
    win.move(0, 3)
    win.clrtobot()
    self.assertEqual(win.instr(0, 0).rstrip(), b'Lor')
    self.assertEqual(win.instr(1, 0).rstrip(), b'')
    for func in [win.erase, win.clear]:
        lorem_ipsum(win)
        func()
        self.assertEqual(win.instr(0, 0).rstrip(), b'')
        self.assertEqual(win.instr(1, 0).rstrip(), b'')
