# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_color_content

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(curses.color_content(curses.COLOR_BLACK), (0, 0, 0))
    curses.color_content(0)
    maxcolor = curses.COLORS - 1
    curses.color_content(maxcolor)
    for color in self.bad_colors():
        self.assertRaises(ValueError, curses.color_content, color)
