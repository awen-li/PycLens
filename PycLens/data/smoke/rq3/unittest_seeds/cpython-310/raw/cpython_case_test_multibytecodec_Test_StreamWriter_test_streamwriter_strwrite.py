# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_StreamWriter_test_streamwriter_strwrite

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = io.BytesIO()
    wr = codecs.getwriter('gb18030')(s)
    wr.write('abcd')
    self.assertEqual(s.getvalue(), b'abcd')
