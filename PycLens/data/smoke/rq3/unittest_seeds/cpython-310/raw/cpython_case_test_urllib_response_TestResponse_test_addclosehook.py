# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib_response.py
# case: TestResponse_test_addclosehook

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    closehook_called = False

    def closehook():
        nonlocal closehook_called
        closehook_called = True
    closehook = urllib.response.addclosehook(self.fp, closehook)
    closehook.close()
    self.assertTrue(self.fp.closed)
    self.assertTrue(closehook_called)
