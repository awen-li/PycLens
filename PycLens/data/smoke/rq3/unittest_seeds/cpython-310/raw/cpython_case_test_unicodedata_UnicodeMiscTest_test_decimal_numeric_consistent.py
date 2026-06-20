# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicodedata.py
# case: UnicodeMiscTest_test_decimal_numeric_consistent

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    count = 0
    for i in range(65536):
        c = chr(i)
        dec = self.db.decimal(c, -1)
        if dec != -1:
            self.assertEqual(dec, self.db.numeric(c))
            count += 1
    self.assertTrue(count >= 10)
