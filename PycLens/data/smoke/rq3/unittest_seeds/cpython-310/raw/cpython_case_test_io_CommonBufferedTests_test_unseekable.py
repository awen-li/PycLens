# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CommonBufferedTests_test_unseekable

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    bufio = self.tp(self.MockUnseekableIO(b'A' * 10))
    self.assertRaises(self.UnsupportedOperation, bufio.tell)
    self.assertRaises(self.UnsupportedOperation, bufio.seek, 0)
