# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hash.py
# case: HashDistributionTestCase_test_hash_distribution

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    base = 'abcdefghabcdefg'
    for i in range(1, len(base)):
        prefix = base[:i]
        with self.subTest(prefix=prefix):
            s15 = set()
            s255 = set()
            for c in range(256):
                h = hash(prefix + chr(c))
                s15.add(h & 15)
                s255.add(h & 255)
            self.assertGreater(len(s15), 8, prefix)
            self.assertGreater(len(s255), 128, prefix)
