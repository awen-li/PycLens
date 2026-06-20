# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_sys_setprofile.py
# case: TestGetProfile_test_setget

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fn(*args):
        pass
    sys.setprofile(fn)
    self.assertIs(sys.getprofile(), fn)
