# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_weakref.py
# case: ReferencesTestCase_test_cfunction

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    create_cfunction = _testcapi.create_cfunction
    f = create_cfunction()
    wr = weakref.ref(f)
    self.assertIs(wr(), f)
    del f
    self.assertIsNone(wr())
    self.check_basic_ref(create_cfunction)
    self.check_basic_callback(create_cfunction)
