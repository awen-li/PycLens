# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_digest_length_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    large_sizes = (2 ** 29, 2 ** 32 - 10, 2 ** 32 + 10, 2 ** 61, 2 ** 64 - 10, 2 ** 64 + 10)
    for cons in self.hash_constructors:
        h = cons(usedforsecurity=False)
        if h.name not in self.shakes:
            continue
        if HASH is not None and isinstance(h, HASH):
            continue
        for digest in (h.digest, h.hexdigest):
            self.assertRaises(ValueError, digest, -10)
            for length in large_sizes:
                with self.assertRaises((ValueError, OverflowError)):
                    digest(length)
