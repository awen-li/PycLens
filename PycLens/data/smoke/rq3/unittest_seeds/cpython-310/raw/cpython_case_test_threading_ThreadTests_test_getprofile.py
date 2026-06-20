# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_threading.py
# case: ThreadTests_test_getprofile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def fn(*args):
        pass
    old_profile = threading.getprofile()
    try:
        threading.setprofile(fn)
        self.assertEqual(fn, threading.getprofile())
    finally:
        threading.setprofile(old_profile)
