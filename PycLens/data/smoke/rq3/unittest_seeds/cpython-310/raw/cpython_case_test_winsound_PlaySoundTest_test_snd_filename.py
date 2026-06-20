# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: PlaySoundTest_test_snd_filename

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fn = support.findfile('pluck-pcm8.wav', subdir='audiodata')
    safe_PlaySound(fn, winsound.SND_FILENAME | winsound.SND_NODEFAULT)
