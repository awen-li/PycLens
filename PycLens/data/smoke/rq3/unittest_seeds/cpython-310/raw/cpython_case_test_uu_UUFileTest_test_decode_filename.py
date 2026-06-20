# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUFileTest_test_decode_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.tmpin, 'wb') as f:
        f.write(encodedtextwrapped(420, self.tmpout))
    uu.decode(self.tmpin)
    with open(self.tmpout, 'rb') as f:
        s = f.read()
    self.assertEqual(s, plaintext)
