# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_issue21088

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    try:
        signature = inspect.signature(stdscr.addch)
        self.assertFalse(signature)
    except ValueError:
        pass
    human_readable_signature = stdscr.addch.__doc__.split('\n')[0]
    self.assertIn('[y, x,]', human_readable_signature)
