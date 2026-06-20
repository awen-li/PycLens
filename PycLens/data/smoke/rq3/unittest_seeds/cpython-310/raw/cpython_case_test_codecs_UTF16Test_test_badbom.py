# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF16Test_test_badbom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = io.BytesIO(b'\xff\xff')
    f = codecs.getreader(self.encoding)(s)
    self.assertRaises(UnicodeError, f.read)
    s = io.BytesIO(b'\xff\xff\xff\xff')
    f = codecs.getreader(self.encoding)(s)
    self.assertRaises(UnicodeError, f.read)
