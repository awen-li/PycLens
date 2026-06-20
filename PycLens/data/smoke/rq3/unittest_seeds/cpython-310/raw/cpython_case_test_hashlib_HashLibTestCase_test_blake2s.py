# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_blake2s

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_blake2(hashlib.blake2s, 8, 8, 32, 32, (1 << 48) - 1)
    b2s_md_len = [16, 20, 28, 32]
    b2s_in_len = [0, 3, 64, 65, 255, 1024]
    self.assertEqual(self.blake2_rfc7693(hashlib.blake2s, b2s_md_len, b2s_in_len), '6a411f08ce25adcdfb02aba641451cec53c598b24f4fc787fbdc88797f4c1dfe')
