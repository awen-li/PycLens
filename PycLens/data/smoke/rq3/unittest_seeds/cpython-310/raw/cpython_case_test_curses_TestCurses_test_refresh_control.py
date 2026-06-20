# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_refresh_control

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdscr = self.stdscr
    stdscr.refresh()
    self.assertIs(stdscr.is_wintouched(), False)
    stdscr.touchwin()
    self.assertIs(stdscr.is_wintouched(), True)
    stdscr.refresh()
    self.assertIs(stdscr.is_wintouched(), False)
    stdscr.touchwin()
    self.assertIs(stdscr.is_wintouched(), True)
    stdscr.untouchwin()
    self.assertIs(stdscr.is_wintouched(), False)
    stdscr.touchline(5, 2)
    self.assertIs(stdscr.is_linetouched(5), True)
    self.assertIs(stdscr.is_linetouched(6), True)
    self.assertIs(stdscr.is_wintouched(), True)
    stdscr.touchline(5, 1, False)
    self.assertIs(stdscr.is_linetouched(5), False)
    win = stdscr.subwin(10, 15, 2, 5)
    win2 = win.subwin(5, 10, 3, 7)
    win2.touchwin()
    stdscr.untouchwin()
    win2.syncup()
    self.assertIs(win.is_wintouched(), True)
    self.assertIs(stdscr.is_wintouched(), True)
    stdscr.touchwin()
    win.untouchwin()
    win2.untouchwin()
    win2.syncdown()
    self.assertIs(win2.is_wintouched(), True)
    if hasattr(stdscr, 'syncok') and (not sys.platform.startswith('sunos')):
        win.untouchwin()
        stdscr.untouchwin()
        for syncok in [False, True]:
            win2.syncok(syncok)
            win2.addch('a')
            self.assertIs(win.is_wintouched(), syncok)
            self.assertIs(stdscr.is_wintouched(), syncok)
