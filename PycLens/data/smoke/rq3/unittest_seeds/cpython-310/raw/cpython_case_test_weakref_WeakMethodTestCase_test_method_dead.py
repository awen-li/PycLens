# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: WeakMethodTestCase_test_method_dead

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    C = self._subclass()
    o = C(1)
    r = weakref.WeakMethod(o.some_method)
    del C.some_method
    gc.collect()
    self.assertIs(r(), None)
