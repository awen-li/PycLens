# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: URandomTests_test_urandom_subprocess

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data1 = self.get_urandom_subprocess(16)
    data2 = self.get_urandom_subprocess(16)
    self.assertNotEqual(data1, data2)
