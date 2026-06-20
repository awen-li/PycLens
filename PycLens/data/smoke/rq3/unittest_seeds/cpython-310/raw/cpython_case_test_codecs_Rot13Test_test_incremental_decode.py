# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Rot13Test_test_incremental_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    decoder = codecs.getincrementaldecoder('rot-13')()
    plaintext = decoder.decode('terra Ares envy tha')
    self.assertEqual(plaintext, 'green Nerf rail gun')
