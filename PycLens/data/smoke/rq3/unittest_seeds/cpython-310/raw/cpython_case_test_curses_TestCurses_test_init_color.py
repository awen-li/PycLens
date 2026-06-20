# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_init_color

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if not curses.can_change_color():
        self.skipTest('cannot change color')
    old = curses.color_content(0)
    try:
        curses.init_color(0, *old)
    except curses.error:
        self.skipTest('cannot change color (init_color() failed)')
    self.addCleanup(curses.init_color, 0, *old)
    curses.init_color(0, 0, 0, 0)
    self.assertEqual(curses.color_content(0), (0, 0, 0))
    curses.init_color(0, 1000, 1000, 1000)
    self.assertEqual(curses.color_content(0), (1000, 1000, 1000))
    maxcolor = curses.COLORS - 1
    old = curses.color_content(maxcolor)
    curses.init_color(maxcolor, *old)
    self.addCleanup(curses.init_color, maxcolor, *old)
    curses.init_color(maxcolor, 0, 500, 1000)
    self.assertEqual(curses.color_content(maxcolor), (0, 500, 1000))
    for color in self.bad_colors():
        self.assertRaises(ValueError, curses.init_color, color, 0, 0, 0)
    for comp in (-1, 1001):
        self.assertRaises(ValueError, curses.init_color, 0, comp, 0, 0)
        self.assertRaises(ValueError, curses.init_color, 0, 0, comp, 0)
        self.assertRaises(ValueError, curses.init_color, 0, 0, 0, comp)
