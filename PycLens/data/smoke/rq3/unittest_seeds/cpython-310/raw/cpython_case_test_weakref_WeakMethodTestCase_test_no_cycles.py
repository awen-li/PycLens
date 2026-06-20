# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: WeakMethodTestCase_test_no_cycles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = Object(1)

    def cb(_):
        pass
    r = weakref.WeakMethod(o.some_method, cb)
    wr = weakref.ref(r)
    del r
    self.assertIs(wr(), None)
