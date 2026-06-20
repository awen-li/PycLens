# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_call.py
# case: TestPEP590_test_vectorcall_flag

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(_testcapi.MethodDescriptorBase.__flags__ & Py_TPFLAGS_HAVE_VECTORCALL)
    self.assertTrue(_testcapi.MethodDescriptorDerived.__flags__ & Py_TPFLAGS_HAVE_VECTORCALL)
    self.assertFalse(_testcapi.MethodDescriptorNopGet.__flags__ & Py_TPFLAGS_HAVE_VECTORCALL)
    self.assertTrue(_testcapi.MethodDescriptor2.__flags__ & Py_TPFLAGS_HAVE_VECTORCALL)

    class MethodDescriptorHeap(_testcapi.MethodDescriptorBase):
        pass
    self.assertFalse(MethodDescriptorHeap.__flags__ & Py_TPFLAGS_HAVE_VECTORCALL)
