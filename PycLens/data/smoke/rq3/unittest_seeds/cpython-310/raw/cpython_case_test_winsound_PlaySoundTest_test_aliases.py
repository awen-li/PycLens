# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_winsound.py
# case: PlaySoundTest_test_aliases

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    aliases = ['SystemAsterisk', 'SystemExclamation', 'SystemExit', 'SystemHand', 'SystemQuestion']
    for alias in aliases:
        with self.subTest(alias=alias):
            safe_PlaySound(alias, winsound.SND_ALIAS)
