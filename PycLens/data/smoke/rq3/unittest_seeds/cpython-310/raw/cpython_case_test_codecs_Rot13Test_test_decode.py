# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: Rot13Test_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    plaintext = codecs.decode('Rg gh, Oehgr?', 'rot-13')
    self.assertEqual(plaintext, 'Et tu, Brute?')
