# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_aifc.py
# case: AIFCLowLevelTest_test_write_aiff_by_extension

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sampwidth = 2
    filename = TESTFN + '.aiff'
    fout = self.fout = aifc.open(filename, 'wb')
    self.addCleanup(unlink, filename)
    fout.setparams((1, sampwidth, 1, 1, b'ULAW', b''))
    frames = b'\x00' * fout.getnchannels() * sampwidth
    fout.writeframes(frames)
    fout.close()
    f = self.f = aifc.open(filename, 'rb')
    self.assertEqual(f.getcomptype(), b'NONE')
    f.close()
