# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_usedforsecurity_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hashlib.new('sha256', usedforsecurity=True)
    if self.is_fips_mode:
        self.skipTest('skip in FIPS mode')
    for cons in self.hash_constructors:
        cons(usedforsecurity=True)
        cons(b'', usedforsecurity=True)
    hashlib.new('md5', usedforsecurity=True)
    hashlib.md5(usedforsecurity=True)
    if self._hashlib is not None:
        self._hashlib.new('md5', usedforsecurity=True)
        self._hashlib.openssl_md5(usedforsecurity=True)
