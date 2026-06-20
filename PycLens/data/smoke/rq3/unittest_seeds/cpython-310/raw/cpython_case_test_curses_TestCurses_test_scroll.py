# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_scroll

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    win = curses.newwin(5, 15, 5, 2)
    lorem_ipsum(win)
    win.scrollok(True)
    win.scroll()
    self.assertEqual(win.instr(0, 0), b'dolor sit amet,')
    win.scroll(2)
    self.assertEqual(win.instr(0, 0), b'adipiscing elit')
    win.scroll(-3)
    self.assertEqual(win.instr(0, 0), b'               ')
    self.assertEqual(win.instr(2, 0), b'               ')
    self.assertEqual(win.instr(3, 0), b'adipiscing elit')
    win.scrollok(False)
