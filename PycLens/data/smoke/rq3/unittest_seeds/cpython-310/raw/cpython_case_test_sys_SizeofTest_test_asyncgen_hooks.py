# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys.py
# case: SizeofTest_test_asyncgen_hooks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old = sys.get_asyncgen_hooks()
    self.assertIsNone(old.firstiter)
    self.assertIsNone(old.finalizer)
    firstiter = lambda *a: None
    sys.set_asyncgen_hooks(firstiter=firstiter)
    hooks = sys.get_asyncgen_hooks()
    self.assertIs(hooks.firstiter, firstiter)
    self.assertIs(hooks[0], firstiter)
    self.assertIs(hooks.finalizer, None)
    self.assertIs(hooks[1], None)
    finalizer = lambda *a: None
    sys.set_asyncgen_hooks(finalizer=finalizer)
    hooks = sys.get_asyncgen_hooks()
    self.assertIs(hooks.firstiter, firstiter)
    self.assertIs(hooks[0], firstiter)
    self.assertIs(hooks.finalizer, finalizer)
    self.assertIs(hooks[1], finalizer)
    sys.set_asyncgen_hooks(*old)
    cur = sys.get_asyncgen_hooks()
    self.assertIsNone(cur.firstiter)
    self.assertIsNone(cur.finalizer)
