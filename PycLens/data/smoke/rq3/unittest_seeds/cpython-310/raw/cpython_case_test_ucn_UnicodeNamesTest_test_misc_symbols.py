# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_misc_symbols

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkletter('PILCROW SIGN', '¶')
    self.checkletter('REPLACEMENT CHARACTER', '�')
    self.checkletter('HALFWIDTH KATAKANA SEMI-VOICED SOUND MARK', 'ﾟ')
    self.checkletter('FULLWIDTH LATIN SMALL LETTER A', 'ａ')
