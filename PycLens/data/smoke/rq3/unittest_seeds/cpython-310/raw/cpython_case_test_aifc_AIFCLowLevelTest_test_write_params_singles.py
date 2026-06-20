# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_write_params_singles

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fout = aifc.open(io.BytesIO(), 'wb')
    fout.aifc()
    fout.setnchannels(1)
    fout.setsampwidth(2)
    fout.setframerate(3)
    fout.setnframes(4)
    fout.setcomptype(b'NONE', b'name')
    self.assertEqual(fout.getnchannels(), 1)
    self.assertEqual(fout.getsampwidth(), 2)
    self.assertEqual(fout.getframerate(), 3)
    self.assertEqual(fout.getnframes(), 0)
    self.assertEqual(fout.tell(), 0)
    self.assertEqual(fout.getcomptype(), b'NONE')
    self.assertEqual(fout.getcompname(), b'name')
    fout.writeframes(b'\x00' * 4 * fout.getsampwidth() * fout.getnchannels())
    self.assertEqual(fout.getnframes(), 4)
    self.assertEqual(fout.tell(), 4)
