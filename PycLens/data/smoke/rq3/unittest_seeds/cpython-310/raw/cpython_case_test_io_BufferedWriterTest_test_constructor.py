# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MockRawIO()
    bufio = self.tp(rawio)
    bufio.__init__(rawio)
    bufio.__init__(rawio, buffer_size=1024)
    bufio.__init__(rawio, buffer_size=16)
    self.assertEqual(3, bufio.write(b'abc'))
    bufio.flush()
    self.assertRaises(ValueError, bufio.__init__, rawio, buffer_size=0)
    self.assertRaises(ValueError, bufio.__init__, rawio, buffer_size=-16)
    self.assertRaises(ValueError, bufio.__init__, rawio, buffer_size=-1)
    bufio.__init__(rawio)
    self.assertEqual(3, bufio.write(b'ghi'))
    bufio.flush()
    self.assertEqual(b''.join(rawio._write_stack), b'abcghi')
