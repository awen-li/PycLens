# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestTracebackException_test_long_context_chain

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        try:
            1 / 0
        except:
            f()
    try:
        f()
    except RecursionError:
        exc_info = sys.exc_info()
    else:
        self.fail('Exception not raised')
    te = traceback.TracebackException(*exc_info)
    res = list(te.format())
    self.assertGreater(len(res), sys.getrecursionlimit())
    self.assertGreater(len([l for l in res if 'ZeroDivisionError:' in l]), sys.getrecursionlimit() * 0.5)
    self.assertIn('RecursionError: maximum recursion depth exceeded', res[-1])
