# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_pyexpat.py
# case: ChardataBufferTest_test_wrong_size

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    parser = expat.ParserCreate()
    parser.buffer_text = 1
    with self.assertRaises(ValueError):
        parser.buffer_size = -1
    with self.assertRaises(ValueError):
        parser.buffer_size = 0
    with self.assertRaises((ValueError, OverflowError)):
        parser.buffer_size = sys.maxsize + 1
    with self.assertRaises(TypeError):
        parser.buffer_size = 512.0
