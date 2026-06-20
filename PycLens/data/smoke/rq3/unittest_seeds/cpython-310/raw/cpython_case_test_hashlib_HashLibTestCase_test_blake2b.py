# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_hashlib.py
# case: HashLibTestCase_test_blake2b

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_blake2(hashlib.blake2b, 16, 16, 64, 64, (1 << 64) - 1)
    b2b_md_len = [20, 32, 48, 64]
    b2b_in_len = [0, 3, 128, 129, 255, 1024]
    self.assertEqual(self.blake2_rfc7693(hashlib.blake2b, b2b_md_len, b2b_in_len), 'c23a7800d98123bd10f506c61e29da5603d763b8bbad2e737f5e765a7bccd475')
