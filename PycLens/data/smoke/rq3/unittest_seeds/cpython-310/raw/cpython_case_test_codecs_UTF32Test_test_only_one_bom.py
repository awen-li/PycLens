# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_codecs.py
# case: UTF32Test_test_only_one_bom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (_, _, reader, writer) = codecs.lookup(self.encoding)
    s = io.BytesIO()
    f = writer(s)
    f.write('spam')
    f.write('spam')
    d = s.getvalue()
    self.assertTrue(d == self.spamle or d == self.spambe)
    s = io.BytesIO(d)
    f = reader(s)
    self.assertEqual(f.read(), 'spamspam')
