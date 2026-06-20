# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_output_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    stdscr.clearok(True)
    stdscr.clearok(False)
    stdscr.idcok(True)
    stdscr.idcok(False)
    stdscr.idlok(False)
    stdscr.idlok(True)
    if hasattr(stdscr, 'immedok'):
        stdscr.immedok(True)
        stdscr.immedok(False)
    stdscr.leaveok(True)
    stdscr.leaveok(False)
    stdscr.scrollok(True)
    stdscr.scrollok(False)
    stdscr.setscrreg(5, 10)
    curses.nonl()
    curses.nl(True)
    curses.nl(False)
    curses.nl()
