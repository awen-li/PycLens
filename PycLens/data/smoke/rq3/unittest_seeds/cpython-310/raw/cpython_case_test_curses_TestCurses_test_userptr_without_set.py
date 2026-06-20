# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_userptr_without_set

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = curses.newwin(10, 10)
    p = curses.panel.new_panel(w)
    with self.assertRaises(curses.panel.error, msg='userptr should fail since not set'):
        p.userptr()
