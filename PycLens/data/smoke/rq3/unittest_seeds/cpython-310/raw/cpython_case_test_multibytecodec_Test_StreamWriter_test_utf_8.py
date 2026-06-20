# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_StreamWriter_test_utf_8

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = io.BytesIO()
    c = codecs.getwriter('utf-8')(s)
    c.write('123')
    self.assertEqual(s.getvalue(), b'123')
    c.write('𒍅')
    self.assertEqual(s.getvalue(), b'123\xf0\x92\x8d\x85')
    c.write('가¬')
    self.assertEqual(s.getvalue(), b'123\xf0\x92\x8d\x85\xea\xb0\x80\xc2\xac')
