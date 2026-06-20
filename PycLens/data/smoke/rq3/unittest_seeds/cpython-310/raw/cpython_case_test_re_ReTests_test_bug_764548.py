# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_764548

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class my_unicode(str):
        pass
    pat = re.compile(my_unicode('abc'))
    self.assertIsNone(pat.match('xyz'))
