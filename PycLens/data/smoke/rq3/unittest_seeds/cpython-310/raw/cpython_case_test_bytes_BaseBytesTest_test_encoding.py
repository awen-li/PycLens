# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = 'Hello world\nሴ噸骼'
    for enc in ('utf-8', 'utf-16'):
        b = self.type2test(sample, enc)
        self.assertEqual(b, self.type2test(sample.encode(enc)))
    self.assertRaises(UnicodeEncodeError, self.type2test, sample, 'latin-1')
    b = self.type2test(sample, 'latin-1', 'ignore')
    self.assertEqual(b, self.type2test(sample[:-3], 'utf-8'))
