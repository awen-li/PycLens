# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_itertools.py
# case: TestBasicOps_test_zip_longest_pickling

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for proto in range(pickle.HIGHEST_PROTOCOL + 1):
        self.pickletest(proto, zip_longest('abc', 'def'))
        self.pickletest(proto, zip_longest('abc', 'defgh'))
        self.pickletest(proto, zip_longest('abc', 'defgh', fillvalue=1))
        self.pickletest(proto, zip_longest('', 'defgh'))
