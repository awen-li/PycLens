# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_latin_modifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('be_BY.UTF-8@latin', 'be_BY.UTF-8@latin')
    self.check('sr_RS.UTF-8@latin', 'sr_RS.UTF-8@latin')
    self.check('sr_RS.UTF-8@latn', 'sr_RS.UTF-8@latin')
