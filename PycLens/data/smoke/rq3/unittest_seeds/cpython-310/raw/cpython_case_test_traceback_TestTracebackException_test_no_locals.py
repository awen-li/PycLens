# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_no_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.updatecache('/foo.py', globals())
    e = Exception('uh oh')
    c = test_code('/foo.py', 'method')
    f = test_frame(c, globals(), {'something': 1})
    tb = test_tb(f, 6, None)
    exc = traceback.TracebackException(Exception, e, tb)
    self.assertEqual(exc.stack[0].locals, None)
