# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: StreamRecoderTest_test_seeking_read

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = io.BytesIO('line1\nline2\nline3\n'.encode('utf-16-le'))
    sr = codecs.EncodedFile(bio, 'utf-8', 'utf-16-le')
    self.assertEqual(sr.readline(), b'line1\n')
    sr.seek(0)
    self.assertEqual(sr.readline(), b'line1\n')
    self.assertEqual(sr.readline(), b'line2\n')
    self.assertEqual(sr.readline(), b'line3\n')
    self.assertEqual(sr.readline(), b'')
