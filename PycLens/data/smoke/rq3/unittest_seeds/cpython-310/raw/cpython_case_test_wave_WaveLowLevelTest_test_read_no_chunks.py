# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wave.py
# case: WaveLowLevelTest_test_read_no_chunks

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    b = b'SPAM'
    with self.assertRaises(EOFError):
        wave.open(io.BytesIO(b))
