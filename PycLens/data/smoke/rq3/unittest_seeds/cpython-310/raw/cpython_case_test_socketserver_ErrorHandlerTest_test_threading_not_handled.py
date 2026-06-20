# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: ErrorHandlerTest_test_threading_not_handled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with threading_helper.catch_threading_exception() as cm:
        ThreadingErrorTestServer(SystemExit)
        self.check_result(handled=False)
        self.assertIs(cm.exc_type, SystemExit)
