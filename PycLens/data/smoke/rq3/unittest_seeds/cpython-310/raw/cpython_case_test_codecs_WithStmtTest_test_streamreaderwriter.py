# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: WithStmtTest_test_streamreaderwriter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO(b'\xc3\xbc')
    info = codecs.lookup('utf-8')
    with codecs.StreamReaderWriter(f, info.streamreader, info.streamwriter, 'strict') as srw:
        self.assertEqual(srw.read(), 'ü')
