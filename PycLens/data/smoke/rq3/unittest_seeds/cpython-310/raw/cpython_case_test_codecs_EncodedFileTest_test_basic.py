# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: EncodedFileTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO(b'\xed\x95\x9c\n\xea\xb8\x80')
    ef = codecs.EncodedFile(f, 'utf-16-le', 'utf-8')
    self.assertEqual(ef.read(), b'\\\xd5\n\x00\x00\xae')
    f = io.BytesIO()
    ef = codecs.EncodedFile(f, 'utf-8', 'latin-1')
    ef.write(b'\xc3\xbc')
    self.assertEqual(f.getvalue(), b'\xfc')
