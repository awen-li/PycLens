# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_comparison_params_variations

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def raise_exc():
        try:
            raise ValueError('bad value')
        except:
            raise

    def raise_with_locals():
        (x, y) = (1, 2)
        raise_exc()
    try:
        raise_with_locals()
    except Exception:
        exc_info = sys.exc_info()
    exc = traceback.TracebackException(*exc_info)
    exc1 = traceback.TracebackException(*exc_info, limit=10)
    exc2 = traceback.TracebackException(*exc_info, limit=2)
    self.assertEqual(exc, exc1)
    self.assertNotEqual(exc, exc2)
    exc3 = traceback.TracebackException(*exc_info, capture_locals=True)
    self.assertNotEqual(exc, exc3)
    exc4 = traceback.TracebackException(*exc_info, limit=-1)
    exc5 = traceback.TracebackException(*exc_info, limit=-1, capture_locals=True)
    self.assertEqual(exc4, exc5)
    exc6 = traceback.TracebackException(*exc_info, limit=-2)
    exc7 = traceback.TracebackException(*exc_info, limit=-2, capture_locals=True)
    self.assertNotEqual(exc6, exc7)
