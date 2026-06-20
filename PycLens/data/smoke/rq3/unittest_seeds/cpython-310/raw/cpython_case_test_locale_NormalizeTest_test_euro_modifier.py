# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_euro_modifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('de_DE@euro', 'de_DE.ISO8859-15')
    self.check('en_US.ISO8859-15@euro', 'en_US.ISO8859-15')
    self.check('de_DE.utf8@euro', 'de_DE.UTF-8')
