# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_bug1098990_a

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = 'xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx yyyyyyyyyyyyyyyyyyyyyyyyyyyyyyy\r\n'
    s2 = 'offending line: ladfj askldfj klasdj fskla dfzaskdj fasklfj laskd fjasklfzzzzaa%whereisthis!!!\r\n'
    s3 = 'next line.\r\n'
    s = (s1 + s2 + s3).encode(self.encoding)
    stream = io.BytesIO(s)
    reader = codecs.getreader(self.encoding)(stream)
    self.assertEqual(reader.readline(), s1)
    self.assertEqual(reader.readline(), s2)
    self.assertEqual(reader.readline(), s3)
    self.assertEqual(reader.readline(), '')
