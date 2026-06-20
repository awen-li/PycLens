# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: WithStmtTest_test_encodedfile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO(b'\xc3\xbc')
    with codecs.EncodedFile(f, 'latin-1', 'utf-8') as ef:
        self.assertEqual(ef.read(), b'\xfc')
    self.assertTrue(f.closed)
