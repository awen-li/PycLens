# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_devanagari_modifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('ks_IN.UTF-8@devanagari', 'ks_IN.UTF-8@devanagari')
    self.check('ks_IN@devanagari', 'ks_IN.UTF-8@devanagari')
    self.check('ks@devanagari', 'ks_IN.UTF-8@devanagari')
    self.check('ks_IN.UTF-8', 'ks_IN.UTF-8')
    self.check('ks_IN', 'ks_IN.UTF-8')
    self.check('ks', 'ks_IN.UTF-8')
    self.check('sd_IN.UTF-8@devanagari', 'sd_IN.UTF-8@devanagari')
    self.check('sd_IN@devanagari', 'sd_IN.UTF-8@devanagari')
    self.check('sd@devanagari', 'sd_IN.UTF-8@devanagari')
    self.check('sd_IN.UTF-8', 'sd_IN.UTF-8')
    self.check('sd_IN', 'sd_IN.UTF-8')
    self.check('sd', 'sd_IN.UTF-8')
