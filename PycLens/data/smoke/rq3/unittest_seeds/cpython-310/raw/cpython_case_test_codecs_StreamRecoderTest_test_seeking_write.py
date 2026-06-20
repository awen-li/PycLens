# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: StreamRecoderTest_test_seeking_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = io.BytesIO('123456789\n'.encode('utf-16-le'))
    sr = codecs.EncodedFile(bio, 'utf-8', 'utf-16-le')
    sr.seek(2)
    sr.write(b'\nabc\n')
    self.assertEqual(sr.readline(), b'789\n')
    sr.seek(0)
    self.assertEqual(sr.readline(), b'1\n')
    self.assertEqual(sr.readline(), b'abc\n')
    self.assertEqual(sr.readline(), b'789\n')
