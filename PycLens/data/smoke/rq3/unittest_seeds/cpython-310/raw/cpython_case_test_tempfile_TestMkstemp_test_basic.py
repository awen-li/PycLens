# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkstemp_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.do_create()
    self.do_create(pre='a')
    self.do_create(suf='b')
    self.do_create(pre='a', suf='b')
    self.do_create(pre='aa', suf='.txt')
    self.do_create(dir='.')
