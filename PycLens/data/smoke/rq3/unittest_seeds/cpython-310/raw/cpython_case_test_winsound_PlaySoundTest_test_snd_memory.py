# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: PlaySoundTest_test_snd_memory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with open(support.findfile('pluck-pcm8.wav', subdir='audiodata'), 'rb') as f:
        audio_data = f.read()
    safe_PlaySound(audio_data, winsound.SND_MEMORY)
    audio_data = bytearray(audio_data)
    safe_PlaySound(audio_data, winsound.SND_MEMORY)
