# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binhex.py
# case: BinHexTestCase_test_binhex

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(self.fname1, 'wb') as f:
        f.write(self.DATA)
    binhex.binhex(self.fname1, self.fname2)
    binhex.hexbin(self.fname2, self.fname1)
    with open(self.fname1, 'rb') as f:
        finish = f.readline()
    self.assertEqual(self.DATA, finish)
