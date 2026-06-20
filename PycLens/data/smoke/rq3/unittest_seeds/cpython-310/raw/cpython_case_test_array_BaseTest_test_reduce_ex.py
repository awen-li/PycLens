# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_array.py
# case: BaseTest_test_reduce_ex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    a = array.array(self.typecode, self.example)
    for protocol in range(3):
        self.assertIs(a.__reduce_ex__(protocol)[0], array.array)
    for protocol in range(3, pickle.HIGHEST_PROTOCOL + 1):
        self.assertIs(a.__reduce_ex__(protocol)[0], array_reconstructor)
