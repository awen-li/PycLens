# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ChardataBufferTest_test_unchanged_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml1 = b"<?xml version='1.0' encoding='iso8859'?><s>" + b'a' * 512
    xml2 = b'a' * 512 + b'</s>'
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = self.counting_handler
    parser.buffer_size = 512
    parser.buffer_text = 1
    self.n = 0
    parser.Parse(xml1)
    self.assertEqual(self.n, 1)
    parser.buffer_size = parser.buffer_size
    self.assertEqual(self.n, 1)
    parser.Parse(xml2)
    self.assertEqual(self.n, 2)
