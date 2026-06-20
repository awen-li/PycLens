# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uu.py
# case: UUFileTest_test_encode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.tmpin, 'wb') as fin:
        fin.write(plaintext)
    with open(self.tmpin, 'rb') as fin:
        with open(self.tmpout, 'wb') as fout:
            uu.encode(fin, fout, self.tmpin, mode=420)
    with open(self.tmpout, 'rb') as fout:
        s = fout.read()
    self.assertEqual(s, encodedtextwrapped(420, self.tmpin))
    uu.encode(self.tmpin, self.tmpout, self.tmpin, mode=420)
    with open(self.tmpout, 'rb') as fout:
        s = fout.read()
    self.assertEqual(s, encodedtextwrapped(420, self.tmpin))
