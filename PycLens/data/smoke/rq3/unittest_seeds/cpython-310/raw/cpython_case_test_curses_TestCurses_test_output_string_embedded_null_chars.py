# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_output_string_embedded_null_chars

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    for arg in ['a\x00', b'a\x00']:
        with self.subTest(arg=arg):
            self.assertRaises(ValueError, stdscr.addstr, arg)
            self.assertRaises(ValueError, stdscr.addnstr, arg, 1)
            self.assertRaises(ValueError, stdscr.insstr, arg)
            self.assertRaises(ValueError, stdscr.insnstr, arg, 1)
