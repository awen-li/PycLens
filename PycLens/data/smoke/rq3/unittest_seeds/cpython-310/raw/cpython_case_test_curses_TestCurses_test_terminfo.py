# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_terminfo

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIsInstance(curses.tigetflag('hc'), int)
    self.assertEqual(curses.tigetflag('cols'), -1)
    self.assertEqual(curses.tigetflag('cr'), -1)
    self.assertIsInstance(curses.tigetnum('cols'), int)
    self.assertEqual(curses.tigetnum('hc'), -2)
    self.assertEqual(curses.tigetnum('cr'), -2)
    self.assertIsInstance(curses.tigetstr('cr'), (bytes, type(None)))
    self.assertIsNone(curses.tigetstr('hc'))
    self.assertIsNone(curses.tigetstr('cols'))
    cud = curses.tigetstr('cud')
    if cud is not None:
        self.assertIsInstance(cud, bytes)
        curses.tparm(cud, 2)
        cud_2 = curses.tparm(cud, 2)
        self.assertIsInstance(cud_2, bytes)
        curses.putp(cud_2)
    curses.putp(b'abc\n')
