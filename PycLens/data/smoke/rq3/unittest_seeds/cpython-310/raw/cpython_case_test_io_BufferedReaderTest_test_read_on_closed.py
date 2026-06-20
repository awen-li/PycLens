# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: BufferedReaderTest_test_read_on_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = io.BufferedReader(io.BytesIO(b'12'))
    b.read(1)
    b.close()
    self.assertRaises(ValueError, b.peek)
    self.assertRaises(ValueError, b.read1, 1)
