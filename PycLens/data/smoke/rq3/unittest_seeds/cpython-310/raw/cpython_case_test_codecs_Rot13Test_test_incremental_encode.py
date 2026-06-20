# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Rot13Test_test_incremental_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    encoder = codecs.getincrementalencoder('rot-13')()
    ciphertext = encoder.encode('ABBA nag Cheryl Baker')
    self.assertEqual(ciphertext, 'NOON ant Purely Onxre')
