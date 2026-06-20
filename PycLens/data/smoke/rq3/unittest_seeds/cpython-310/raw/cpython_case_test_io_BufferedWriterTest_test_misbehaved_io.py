# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedWriterTest_test_misbehaved_io

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = self.MisbehavedRawIO()
    bufio = self.tp(rawio, 5)
    self.assertRaises(OSError, bufio.seek, 0)
    self.assertRaises(OSError, bufio.tell)
    self.assertRaises(OSError, bufio.write, b'abcdef')
    bufio.close = lambda : None
