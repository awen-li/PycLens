# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: StreamRecoderTest_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = io.BytesIO()
    codec = codecs.lookup('latin1')
    sr = codecs.StreamRecoder(bio, codec.encode, codec.decode, encodings.utf_8.StreamReader, encodings.utf_8.StreamWriter)
    text = 'àñé'
    sr.write(text.encode('latin1'))
    self.assertEqual(bio.getvalue(), text.encode('utf-8'))
