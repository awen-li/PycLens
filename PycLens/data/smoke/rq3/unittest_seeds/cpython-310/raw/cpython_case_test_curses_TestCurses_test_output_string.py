# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_output_string

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    encoding = stdscr.encoding
    for func in [stdscr.addstr, stdscr.insstr]:
        with self.subTest(func.__qualname__):
            stdscr.move(0, 0)
            func('abcd')
            func(b'abcd')
            s = 'àßçđ'
            try:
                func(s)
            except UnicodeEncodeError:
                self.assertRaises(UnicodeEncodeError, s.encode, encoding)
            func('abcd', curses.A_BOLD)
            func(1, 2, 'abcd')
            func(2, 3, 'abcd', curses.A_BOLD)
    for func in [stdscr.addnstr, stdscr.insnstr]:
        with self.subTest(func.__qualname__):
            stdscr.move(0, 0)
            func('1234', 3)
            func(b'1234', 3)
            s = '١٢٣٤'
            try:
                func(s, 3)
            except UnicodeEncodeError:
                self.assertRaises(UnicodeEncodeError, s.encode, encoding)
            func('1234', 5)
            func('1234', 3, curses.A_BOLD)
            func(1, 2, '1234', 3)
            func(2, 3, '1234', 3, curses.A_BOLD)
