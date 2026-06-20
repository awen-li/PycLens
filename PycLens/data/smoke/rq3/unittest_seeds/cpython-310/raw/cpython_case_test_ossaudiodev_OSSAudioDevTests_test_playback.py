# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ossaudiodev.py
# case: OSSAudioDevTests_test_playback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sound_info = read_sound_file(findfile('audiotest.au'))
    self.play_sound_file(*sound_info)
