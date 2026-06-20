# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_trashcan_16602

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class C:

        def __init__(self, parent):
            if not parent:
                return
            wself = weakref.ref(self)

            def cb(wparent):
                o = wself()
            self.wparent = weakref.ref(parent, cb)
    d = weakref.WeakKeyDictionary()
    root = c = C(None)
    for n in range(100):
        d[c] = c = C(c)
    del root
    gc.collect()
