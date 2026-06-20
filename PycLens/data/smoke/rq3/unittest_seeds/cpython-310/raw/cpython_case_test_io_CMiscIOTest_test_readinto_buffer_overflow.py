# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CMiscIOTest_test_readinto_buffer_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadReader(self.io.BufferedIOBase):

        def read(self, n=-1):
            return b'x' * 10 ** 6
    bufio = BadReader()
    b = bytearray(2)
    self.assertRaises(ValueError, bufio.readinto, b)
