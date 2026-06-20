# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_color_attrs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for pair in (0, 1, 255):
        attr = curses.color_pair(pair)
        self.assertEqual(curses.pair_number(attr), pair, attr)
        self.assertEqual(curses.pair_number(attr | curses.A_BOLD), pair)
    self.assertEqual(curses.color_pair(0), 0)
    self.assertEqual(curses.pair_number(0), 0)
