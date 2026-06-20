# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_basic_ref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_basic_ref(C)
    self.check_basic_ref(create_function)
    self.check_basic_ref(create_bound_method)
    o = C()
    wr = weakref.ref(o)
    repr(wr)
    del o
    repr(wr)
