# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_curs_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (vis, cap) in [(0, 'civis'), (2, 'cvvis'), (1, 'cnorm')]:
        if curses.tigetstr(cap) is not None:
            curses.curs_set(vis)
        else:
            try:
                curses.curs_set(vis)
            except curses.error:
                pass
