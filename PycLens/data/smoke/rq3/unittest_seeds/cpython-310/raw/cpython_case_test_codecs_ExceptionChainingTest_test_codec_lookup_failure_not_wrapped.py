# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: ExceptionChainingTest_test_codec_lookup_failure_not_wrapped

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = '^unknown encoding: {}$'.format(self.codec_name)
    with self.assertRaisesRegex(LookupError, msg):
        'str input'.encode(self.codec_name)
    with self.assertRaisesRegex(LookupError, msg):
        codecs.encode('str input', self.codec_name)
    with self.assertRaisesRegex(LookupError, msg):
        b'bytes input'.decode(self.codec_name)
    with self.assertRaisesRegex(LookupError, msg):
        codecs.decode(b'bytes input', self.codec_name)
