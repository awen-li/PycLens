# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: NormalizeTest_test_hyphenated_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check('az_AZ.iso88599e', 'az_AZ.ISO8859-9E')
    self.check('az_AZ.ISO8859-9E', 'az_AZ.ISO8859-9E')
    self.check('tt_RU.koi8c', 'tt_RU.KOI8-C')
    self.check('tt_RU.KOI8-C', 'tt_RU.KOI8-C')
    self.check('lo_LA.cp1133', 'lo_LA.IBM-CP1133')
    self.check('lo_LA.ibmcp1133', 'lo_LA.IBM-CP1133')
    self.check('lo_LA.IBM-CP1133', 'lo_LA.IBM-CP1133')
    self.check('uk_ua.microsoftcp1251', 'uk_UA.CP1251')
    self.check('uk_ua.microsoft-cp1251', 'uk_UA.CP1251')
    self.check('ka_ge.georgianacademy', 'ka_GE.GEORGIAN-ACADEMY')
    self.check('ka_GE.GEORGIAN-ACADEMY', 'ka_GE.GEORGIAN-ACADEMY')
    self.check('cs_CZ.iso88592', 'cs_CZ.ISO8859-2')
    self.check('cs_CZ.ISO8859-2', 'cs_CZ.ISO8859-2')
