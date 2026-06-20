# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_blake2b_vectors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for (msg, key, md) in read_vectors('blake2b'):
        key = bytes.fromhex(key)
        self.check('blake2b', msg, md, key=key)
