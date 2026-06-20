# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_bytes.py
# case: BaseBytesTest_test_decode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sample = 'Hello world\nሴ噸骼'
    for enc in ('utf-8', 'utf-16'):
        b = self.type2test(sample, enc)
        self.assertEqual(b.decode(enc), sample)
    sample = 'Hello world\n\x80\x81þÿ'
    b = self.type2test(sample, 'latin-1')
    self.assertRaises(UnicodeDecodeError, b.decode, 'utf-8')
    self.assertEqual(b.decode('utf-8', 'ignore'), 'Hello world\n')
    self.assertEqual(b.decode(errors='ignore', encoding='utf-8'), 'Hello world\n')
    self.assertEqual(self.type2test(b'\xe2\x98\x83').decode(), '☃')
