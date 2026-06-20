# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: PlaySoundTest_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, winsound.PlaySound)
    self.assertRaises(TypeError, winsound.PlaySound, 'bad', 'bad')
    self.assertRaises(RuntimeError, winsound.PlaySound, 'none', winsound.SND_ASYNC | winsound.SND_MEMORY)
    self.assertRaises(TypeError, winsound.PlaySound, b'bad', 0)
    self.assertRaises(TypeError, winsound.PlaySound, 'bad', winsound.SND_MEMORY)
    self.assertRaises(TypeError, winsound.PlaySound, 1, 0)
    self.assertRaises(ValueError, winsound.PlaySound, 'bad\x00', 0)
