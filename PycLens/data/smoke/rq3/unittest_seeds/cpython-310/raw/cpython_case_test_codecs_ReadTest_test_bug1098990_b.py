# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ReadTest_test_bug1098990_b

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s1 = 'aaaaaaaaaaaaaaaaaaaaaaaa\r\n'
    s2 = 'bbbbbbbbbbbbbbbbbbbbbbbb\r\n'
    s3 = 'stillokay:bbbbxx\r\n'
    s4 = 'broken!!!!badbad\r\n'
    s5 = 'againokay.\r\n'
    s = (s1 + s2 + s3 + s4 + s5).encode(self.encoding)
    stream = io.BytesIO(s)
    reader = codecs.getreader(self.encoding)(stream)
    self.assertEqual(reader.readline(), s1)
    self.assertEqual(reader.readline(), s2)
    self.assertEqual(reader.readline(), s3)
    self.assertEqual(reader.readline(), s4)
    self.assertEqual(reader.readline(), s5)
    self.assertEqual(reader.readline(), '')
