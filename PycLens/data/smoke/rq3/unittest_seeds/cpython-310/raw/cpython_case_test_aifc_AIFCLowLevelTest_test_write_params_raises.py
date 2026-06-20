# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_write_params_raises

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fout = aifc.open(io.BytesIO(), 'wb')
    wrong_params = (0, 0, 0, 0, b'WRNG', '')
    self.assertRaises(aifc.Error, fout.setparams, wrong_params)
    self.assertRaises(aifc.Error, fout.getparams)
    self.assertRaises(aifc.Error, fout.setnchannels, 0)
    self.assertRaises(aifc.Error, fout.getnchannels)
    self.assertRaises(aifc.Error, fout.setsampwidth, 0)
    self.assertRaises(aifc.Error, fout.getsampwidth)
    self.assertRaises(aifc.Error, fout.setframerate, 0)
    self.assertRaises(aifc.Error, fout.getframerate)
    self.assertRaises(aifc.Error, fout.setcomptype, b'WRNG', '')
    fout.aiff()
    fout.setnchannels(1)
    fout.setsampwidth(1)
    fout.setframerate(1)
    fout.setnframes(1)
    fout.writeframes(b'\x00')
    self.assertRaises(aifc.Error, fout.setparams, (1, 1, 1, 1, 1, 1))
    self.assertRaises(aifc.Error, fout.setnchannels, 1)
    self.assertRaises(aifc.Error, fout.setsampwidth, 1)
    self.assertRaises(aifc.Error, fout.setframerate, 1)
    self.assertRaises(aifc.Error, fout.setnframes, 1)
    self.assertRaises(aifc.Error, fout.setcomptype, b'NONE', '')
    self.assertRaises(aifc.Error, fout.aiff)
    self.assertRaises(aifc.Error, fout.aifc)
