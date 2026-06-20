# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_multibytecodec.py
# case: Test_StreamWriter_test_gb18030

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = io.BytesIO()
    c = codecs.getwriter('gb18030')(s)
    c.write('123')
    self.assertEqual(s.getvalue(), b'123')
    c.write('𒍅')
    self.assertEqual(s.getvalue(), b'123\x907\x959')
    c.write('가¬')
    self.assertEqual(s.getvalue(), b'123\x907\x959\x827\xcf5\x810\x851')
