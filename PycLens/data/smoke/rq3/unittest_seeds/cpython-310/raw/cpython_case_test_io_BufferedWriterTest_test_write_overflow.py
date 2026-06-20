# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_write_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    writer = self.MockRawIO()
    bufio = self.tp(writer, 8)
    contents = b'abcdefghijklmnop'
    for n in range(0, len(contents), 3):
        bufio.write(contents[n:n + 3])
    flushed = b''.join(writer._write_stack)
    self.assertTrue(flushed.startswith(contents[:-8]), flushed)
