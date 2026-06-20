# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestAscii_test_ctrl

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ctrl = curses.ascii.ctrl
    self.assertEqual(ctrl('J'), '\n')
    self.assertEqual(ctrl('\n'), '\n')
    self.assertEqual(ctrl('@'), '\x00')
    self.assertEqual(ctrl(ord('J')), ord('\n'))
