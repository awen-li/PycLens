# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_io.py
# case: CBufferedReaderTest_test_bad_readinto_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rawio = io.BufferedReader(io.BytesIO(b'12'))
    rawio.readinto = lambda buf: -1
    bufio = self.tp(rawio)
    with self.assertRaises(OSError) as cm:
        bufio.readline()
    self.assertIsNone(cm.exception.__cause__)
