# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: GetRandomTests_test_getrandom_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data1 = os.getrandom(16)
    data2 = os.getrandom(16)
    self.assertNotEqual(data1, data2)
