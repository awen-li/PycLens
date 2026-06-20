# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_unget_wch

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    encoding = stdscr.encoding
    for ch in ('a', 'é', '€', '\U0010ffff'):
        try:
            ch.encode(encoding)
        except UnicodeEncodeError:
            continue
        try:
            curses.unget_wch(ch)
        except Exception as err:
            self.fail('unget_wch(%a) failed with encoding %s: %s' % (ch, stdscr.encoding, err))
        read = stdscr.get_wch()
        self.assertEqual(read, ch)
        code = ord(ch)
        curses.unget_wch(code)
        read = stdscr.get_wch()
        self.assertEqual(read, ch)
