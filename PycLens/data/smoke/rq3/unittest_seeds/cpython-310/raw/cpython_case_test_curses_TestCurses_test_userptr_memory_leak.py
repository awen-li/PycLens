# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_curses.py
# case: TestCurses_test_userptr_memory_leak

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = curses.newwin(10, 10)
    p = curses.panel.new_panel(w)
    obj = object()
    nrefs = sys.getrefcount(obj)
    for i in range(100):
        p.set_userptr(obj)
    p.set_userptr(None)
    self.assertEqual(sys.getrefcount(obj), nrefs, 'set_userptr leaked references')
