# Source Generated with Decompyle++
# File: cpython-39-5908e7763464.pyc (Python 3.9)


def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = not None
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

if __name__ == '__main__':
    __pybcsec_seed__()
