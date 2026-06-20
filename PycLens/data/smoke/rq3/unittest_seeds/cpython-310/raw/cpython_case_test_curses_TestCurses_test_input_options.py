# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_input_options

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    if self.isatty:
        curses.nocbreak()
        curses.cbreak()
        curses.cbreak(False)
        curses.cbreak(True)
        curses.intrflush(True)
        curses.intrflush(False)
        curses.raw()
        curses.raw(False)
        curses.raw(True)
        curses.noraw()
    curses.noecho()
    curses.echo()
    curses.echo(False)
    curses.echo(True)
    curses.halfdelay(255)
    curses.halfdelay(1)
    stdscr.keypad(True)
    stdscr.keypad(False)
    curses.meta(True)
    curses.meta(False)
    stdscr.nodelay(True)
    stdscr.nodelay(False)
    curses.noqiflush()
    curses.qiflush(True)
    curses.qiflush(False)
    curses.qiflush()
    stdscr.notimeout(True)
    stdscr.notimeout(False)
    stdscr.timeout(-1)
    stdscr.timeout(0)
    stdscr.timeout(5)
