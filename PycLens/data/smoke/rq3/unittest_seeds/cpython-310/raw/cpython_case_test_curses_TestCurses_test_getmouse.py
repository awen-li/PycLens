# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_getmouse

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (availmask, oldmask) = curses.mousemask(curses.BUTTON1_PRESSED)
    if availmask == 0:
        self.skipTest('mouse stuff not available')
    curses.mouseinterval(10)
    curses.ungetmouse(0, 0, 0, 0, curses.BUTTON1_PRESSED)
    m = curses.getmouse()
