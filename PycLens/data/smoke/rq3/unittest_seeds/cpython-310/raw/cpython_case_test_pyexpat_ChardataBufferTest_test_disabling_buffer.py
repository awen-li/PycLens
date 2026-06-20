# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ChardataBufferTest_test_disabling_buffer

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml1 = b"<?xml version='1.0' encoding='iso8859'?><a>" + b'a' * 512
    xml2 = b'b' * 1024
    xml3 = b'c' * 1024 + b'</a>'
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = self.counting_handler
    parser.buffer_text = 1
    parser.buffer_size = 1024
    self.assertEqual(parser.buffer_size, 1024)
    self.n = 0
    parser.Parse(xml1, False)
    self.assertEqual(parser.buffer_size, 1024)
    self.assertEqual(self.n, 1)
    parser.buffer_text = 0
    self.assertFalse(parser.buffer_text)
    self.assertEqual(parser.buffer_size, 1024)
    for i in range(10):
        parser.Parse(xml2, False)
    self.assertEqual(self.n, 11)
    parser.buffer_text = 1
    self.assertTrue(parser.buffer_text)
    self.assertEqual(parser.buffer_size, 1024)
    parser.Parse(xml3, True)
    self.assertEqual(self.n, 12)
