# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_multiple_selfref_callbacks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def callback(object, self=self):
        self.ref()
    c = C()
    self.ref = weakref.ref(c, callback)
    ref1 = weakref.ref(c, callback)
    del c
