# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_flush

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    writer = self.MockRawIO()
    bufio = self.tp(writer, 8)
    bufio.write(b'abc')
    bufio.flush()
    self.assertEqual(b'abc', writer._write_stack[0])
