# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CBufferedWriterTest_test_constructor

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    BufferedWriterTest.test_constructor(self)
    if sys.maxsize > 2147483647:
        rawio = self.MockRawIO()
        bufio = self.tp(rawio)
        self.assertRaises((OverflowError, MemoryError, ValueError), bufio.__init__, rawio, sys.maxsize)
