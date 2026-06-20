# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_writelines_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    writer = self.MockRawIO()
    bufio = self.tp(writer, 8)
    self.assertRaises(TypeError, bufio.writelines, [1, 2, 3])
    self.assertRaises(TypeError, bufio.writelines, None)
    self.assertRaises(TypeError, bufio.writelines, 'abc')
