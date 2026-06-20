# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: BufferTextTest_test_buffering_enabled

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertTrue(self.parser.buffer_text)
    self.parser.Parse(b'<a>1<b/>2<c/>3</a>', True)
    self.assertEqual(self.stuff, ['123'], 'buffered text not properly collapsed')
