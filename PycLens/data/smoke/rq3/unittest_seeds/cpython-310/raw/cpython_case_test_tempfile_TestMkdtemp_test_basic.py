# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_tempfile.py
# case: TestMkdtemp_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    os.rmdir(self.do_create())
    os.rmdir(self.do_create(pre='a'))
    os.rmdir(self.do_create(suf='b'))
    os.rmdir(self.do_create(pre='a', suf='b'))
    os.rmdir(self.do_create(pre='aa', suf='.txt'))
