# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: TextIOWrapperTest_test_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = self.BytesIO()
    t = self.TextIOWrapper(b, encoding='utf-8')
    self.assertEqual(t.encoding, 'utf-8')
    with warnings.catch_warnings():
        warnings.simplefilter('ignore', EncodingWarning)
        t = self.TextIOWrapper(b)
    self.assertIsNotNone(t.encoding)
    codecs.lookup(t.encoding)
