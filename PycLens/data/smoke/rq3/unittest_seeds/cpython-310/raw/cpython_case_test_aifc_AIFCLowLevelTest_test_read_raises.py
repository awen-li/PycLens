# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_read_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = io.BytesIO(b'\x00')
    self.assertRaises(EOFError, aifc._read_ulong, f)
    self.assertRaises(EOFError, aifc._read_long, f)
    self.assertRaises(EOFError, aifc._read_ushort, f)
    self.assertRaises(EOFError, aifc._read_short, f)
