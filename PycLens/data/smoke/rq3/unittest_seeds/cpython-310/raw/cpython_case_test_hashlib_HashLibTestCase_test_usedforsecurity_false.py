# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_usedforsecurity_false

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    hashlib.new('sha256', usedforsecurity=False)
    for cons in self.hash_constructors:
        cons(usedforsecurity=False)
        cons(b'', usedforsecurity=False)
    hashlib.new('md5', usedforsecurity=False)
    hashlib.md5(usedforsecurity=False)
    if self._hashlib is not None:
        self._hashlib.new('md5', usedforsecurity=False)
        self._hashlib.openssl_md5(usedforsecurity=False)
