# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ChardataBufferTest_test_change_size_1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xml1 = b"<?xml version='1.0' encoding='iso8859'?><a><s>" + b'a' * 1024
    xml2 = b'aaa</s><s>' + b'a' * 1025 + b'</s></a>'
    parser = expat.ParserCreate()
    parser.CharacterDataHandler = self.counting_handler
    parser.buffer_text = 1
    parser.buffer_size = 1024
    self.assertEqual(parser.buffer_size, 1024)
    self.n = 0
    parser.Parse(xml1, False)
    parser.buffer_size *= 2
    self.assertEqual(parser.buffer_size, 2048)
    parser.Parse(xml2, True)
    self.assertEqual(self.n, 2)
