# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestPEP590_test_method_descriptor_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import functools
    cached = functools.lru_cache(1)(testfunction)
    self.assertFalse(type(repr).__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertTrue(type(list.append).__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertTrue(type(list.__add__).__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertTrue(type(testfunction).__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertTrue(type(cached).__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertTrue(_testcapi.MethodDescriptorBase.__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertTrue(_testcapi.MethodDescriptorDerived.__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
    self.assertFalse(_testcapi.MethodDescriptorNopGet.__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)

    class MethodDescriptorHeap(_testcapi.MethodDescriptorBase):
        pass
    self.assertFalse(MethodDescriptorHeap.__flags__ & Py_TPFLAGS_METHOD_DESCRIPTOR)
