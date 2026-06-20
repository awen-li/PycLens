# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CTextIOWrapperTest_test_initialization

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    r = self.BytesIO(b'\xc3\xa9\n\n')
    b = self.BufferedReader(r, 1000)
    t = self.TextIOWrapper(b, encoding='utf-8')
    self.assertRaises(ValueError, t.__init__, b, encoding='utf-8', newline='xyzzy')
    self.assertRaises(ValueError, t.read)
    t = self.TextIOWrapper.__new__(self.TextIOWrapper)
    self.assertRaises(Exception, repr, t)
