# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedRWPairTest_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    w = self.MockRawIO()
    pair = self.tp(self.MockRawIO(), w)
    pair.write(b'abc')
    pair.flush()
    buffer = bytearray(b'def')
    pair.write(buffer)
    buffer[:] = b'***'
    pair.flush()
    self.assertEqual(w._write_stack, [b'abc', b'def'])
