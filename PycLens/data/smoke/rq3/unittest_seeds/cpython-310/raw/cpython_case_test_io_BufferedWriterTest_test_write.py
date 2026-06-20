# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    writer = self.MockRawIO()
    bufio = self.tp(writer, 8)
    bufio.write(b'abc')
    self.assertFalse(writer._write_stack)
    buffer = bytearray(b'def')
    bufio.write(buffer)
    buffer[:] = b'***'
    bufio.flush()
    self.assertEqual(b''.join(writer._write_stack), b'abcdef')
