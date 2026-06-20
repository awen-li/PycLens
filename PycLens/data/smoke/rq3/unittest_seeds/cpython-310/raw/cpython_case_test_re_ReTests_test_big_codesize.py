# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_big_codesize

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = re.compile('|'.join(('%d' % x for x in range(10000))))
    self.assertTrue(r.match('1000'))
    self.assertTrue(r.match('9999'))
