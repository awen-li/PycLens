# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_english

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('en', 'en_US.ISO8859-1')
    self.check('EN', 'en_US.ISO8859-1')
    self.check('en.iso88591', 'en_US.ISO8859-1')
    self.check('en_US', 'en_US.ISO8859-1')
    self.check('en_us', 'en_US.ISO8859-1')
    self.check('en_GB', 'en_GB.ISO8859-1')
    self.check('en_US.UTF-8', 'en_US.UTF-8')
    self.check('en_US.utf8', 'en_US.UTF-8')
    self.check('en_US:UTF-8', 'en_US.UTF-8')
    self.check('en_US.ISO8859-1', 'en_US.ISO8859-1')
    self.check('en_US.US-ASCII', 'en_US.ISO8859-1')
    self.check('en_US.88591', 'en_US.ISO8859-1')
    self.check('en_US.885915', 'en_US.ISO8859-15')
    self.check('english', 'en_EN.ISO8859-1')
    self.check('english_uk.ascii', 'en_GB.ISO8859-1')
