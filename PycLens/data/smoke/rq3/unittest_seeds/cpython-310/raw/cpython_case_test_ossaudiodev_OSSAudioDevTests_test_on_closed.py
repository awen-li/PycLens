# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ossaudiodev.py
# case: OSSAudioDevTests_test_on_closed

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dsp = ossaudiodev.open('w')
    dsp.close()
    self.assertRaises(ValueError, dsp.fileno)
    self.assertRaises(ValueError, dsp.read, 1)
    self.assertRaises(ValueError, dsp.write, b'x')
    self.assertRaises(ValueError, dsp.writeall, b'x')
    self.assertRaises(ValueError, dsp.bufsize)
    self.assertRaises(ValueError, dsp.obufcount)
    self.assertRaises(ValueError, dsp.obufcount)
    self.assertRaises(ValueError, dsp.obuffree)
    self.assertRaises(ValueError, dsp.getptr)
    mixer = ossaudiodev.openmixer()
    mixer.close()
    self.assertRaises(ValueError, mixer.fileno)
