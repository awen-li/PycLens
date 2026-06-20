# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_output_character

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    encoding = stdscr.encoding
    stdscr.refresh()
    stdscr.move(0, 0)
    stdscr.addch('A')
    stdscr.addch(b'A')
    stdscr.addch(65)
    c = '€'
    try:
        stdscr.addch(c)
    except UnicodeEncodeError:
        self.assertRaises(UnicodeEncodeError, c.encode, encoding)
    except OverflowError:
        encoded = c.encode(encoding)
        self.assertNotEqual(len(encoded), 1, repr(encoded))
    stdscr.addch('A', curses.A_BOLD)
    stdscr.addch(1, 2, 'A')
    stdscr.addch(2, 3, 'A', curses.A_BOLD)
    self.assertIs(stdscr.is_wintouched(), True)
    stdscr.refresh()
    stdscr.move(0, 0)
    stdscr.echochar('A')
    stdscr.echochar(b'A')
    stdscr.echochar(65)
    with self.assertRaises((UnicodeEncodeError, OverflowError)):
        stdscr.echochar('Ĕ')
    stdscr.echochar('A', curses.A_BOLD)
    self.assertIs(stdscr.is_wintouched(), False)
