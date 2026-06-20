# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: StreamRecoderTest_test_writelines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bio = io.BytesIO()
    codec = codecs.lookup('ascii')
    sr = codecs.StreamRecoder(bio, codec.encode, codec.decode, encodings.ascii.StreamReader, encodings.ascii.StreamWriter)
    sr.writelines([b'a', b'b'])
    self.assertEqual(bio.getvalue(), b'ab')
