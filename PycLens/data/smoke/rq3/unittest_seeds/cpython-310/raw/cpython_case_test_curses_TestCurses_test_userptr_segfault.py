# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_userptr_segfault

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = curses.newwin(10, 10)
    panel = curses.panel.new_panel(w)

    class A:

        def __del__(self):
            panel.set_userptr(None)
    panel.set_userptr(A())
    panel.set_userptr(None)
