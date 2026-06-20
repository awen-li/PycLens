# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_binhex.py
# case: BinHexTestCase_test_binhex_error_on_long_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f3 = open(self.fname3, 'wb')
    f3.close()
    self.assertRaises(binhex.Error, binhex.binhex, self.fname3, self.fname2)
