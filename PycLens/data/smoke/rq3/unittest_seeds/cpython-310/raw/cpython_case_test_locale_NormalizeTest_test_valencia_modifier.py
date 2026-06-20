# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_valencia_modifier

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('ca_ES.UTF-8@valencia', 'ca_ES.UTF-8@valencia')
    self.check('ca_ES@valencia', 'ca_ES.UTF-8@valencia')
    self.check('ca@valencia', 'ca_ES.ISO8859-1@valencia')
