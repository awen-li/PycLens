# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestAscii_test_ctypes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check(func, expected):
        with self.subTest(ch=c, func=func):
            self.assertEqual(func(i), expected)
            self.assertEqual(func(c), expected)
    for i in range(256):
        c = chr(i)
        b = bytes([i])
        check(curses.ascii.isalnum, b.isalnum())
        check(curses.ascii.isalpha, b.isalpha())
        check(curses.ascii.isdigit, b.isdigit())
        check(curses.ascii.islower, b.islower())
        check(curses.ascii.isspace, b.isspace())
        check(curses.ascii.isupper, b.isupper())
        check(curses.ascii.isascii, i < 128)
        check(curses.ascii.ismeta, i >= 128)
        check(curses.ascii.isctrl, i < 32)
        check(curses.ascii.iscntrl, i < 32 or i == 127)
        check(curses.ascii.isblank, c in ' \t')
        check(curses.ascii.isgraph, 32 < i <= 126)
        check(curses.ascii.isprint, 32 <= i <= 126)
        check(curses.ascii.ispunct, c in string.punctuation)
        check(curses.ascii.isxdigit, c in string.hexdigits)
    for i in (-2, -1, 256, sys.maxunicode, sys.maxunicode + 1):
        self.assertFalse(curses.ascii.isalnum(i))
        self.assertFalse(curses.ascii.isalpha(i))
        self.assertFalse(curses.ascii.isdigit(i))
        self.assertFalse(curses.ascii.islower(i))
        self.assertFalse(curses.ascii.isspace(i))
        self.assertFalse(curses.ascii.isupper(i))
        self.assertFalse(curses.ascii.isascii(i))
        self.assertFalse(curses.ascii.isctrl(i))
        self.assertFalse(curses.ascii.iscntrl(i))
        self.assertFalse(curses.ascii.isblank(i))
        self.assertFalse(curses.ascii.isgraph(i))
        self.assertFalse(curses.ascii.isprint(i))
        self.assertFalse(curses.ascii.ispunct(i))
        self.assertFalse(curses.ascii.isxdigit(i))
    self.assertFalse(curses.ascii.ismeta(-1))
