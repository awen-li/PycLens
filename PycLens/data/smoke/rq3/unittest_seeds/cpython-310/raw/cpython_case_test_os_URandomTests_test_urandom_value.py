# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: URandomTests_test_urandom_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data1 = os.urandom(16)
    self.assertIsInstance(data1, bytes)
    data2 = os.urandom(16)
    self.assertNotEqual(data1, data2)
