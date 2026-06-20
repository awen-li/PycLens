# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUFileTest_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.tmpin, 'wb') as f:
        f.write(encodedtextwrapped(420, self.tmpout))
    with open(self.tmpin, 'rb') as f:
        uu.decode(f)
    with open(self.tmpout, 'rb') as f:
        s = f.read()
    self.assertEqual(s, plaintext)
