# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_gc_during_ref_creation

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_gc_during_creation(weakref.ref)
