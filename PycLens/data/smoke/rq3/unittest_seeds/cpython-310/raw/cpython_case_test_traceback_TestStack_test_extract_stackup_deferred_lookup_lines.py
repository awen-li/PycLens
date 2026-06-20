# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_traceback.py
# case: TestStack_test_extract_stackup_deferred_lookup_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    linecache.clearcache()
    c = test_code('/foo.py', 'method')
    f = test_frame(c, None, None)
    s = traceback.StackSummary.extract(iter([(f, 6)]), lookup_lines=False)
    self.assertEqual({}, linecache.cache)
    linecache.updatecache('/foo.py', globals())
    self.assertEqual(s[0].line, 'import sys')
