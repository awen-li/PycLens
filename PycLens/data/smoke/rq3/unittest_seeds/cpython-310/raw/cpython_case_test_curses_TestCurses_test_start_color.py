# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_start_color

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not curses.has_colors():
        self.skipTest('requires colors support')
    curses.start_color()
    if verbose:
        print(f'COLORS = {curses.COLORS}', file=sys.stderr)
        print(f'COLOR_PAIRS = {curses.COLOR_PAIRS}', file=sys.stderr)
