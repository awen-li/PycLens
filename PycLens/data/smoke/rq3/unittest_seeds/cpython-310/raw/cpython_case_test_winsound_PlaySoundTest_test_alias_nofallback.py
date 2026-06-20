# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: PlaySoundTest_test_alias_nofallback

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    safe_PlaySound('!"$%&/(#+*', winsound.SND_ALIAS | winsound.SND_NODEFAULT)
