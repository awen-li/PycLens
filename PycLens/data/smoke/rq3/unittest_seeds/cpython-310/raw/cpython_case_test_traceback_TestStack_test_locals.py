# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_locals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.updatecache('/foo.py', globals())
    c = test_code('/foo.py', 'method')
    f = test_frame(c, globals(), {'something': 1})
    s = traceback.StackSummary.extract(iter([(f, 6)]), capture_locals=True)
    self.assertEqual(s[0].locals, {'something': '1'})
