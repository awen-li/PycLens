# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ucn.py
# case: UnicodeNamesTest_test_hangul_syllables

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.checkletter('HANGUL SYLLABLE GA', '가')
    self.checkletter('HANGUL SYLLABLE GGWEOSS', '꿨')
    self.checkletter('HANGUL SYLLABLE DOLS', '돐')
    self.checkletter('HANGUL SYLLABLE RYAN', '랸')
    self.checkletter('HANGUL SYLLABLE MWIK', '뮠')
    self.checkletter('HANGUL SYLLABLE BBWAEM', '뾈')
    self.checkletter('HANGUL SYLLABLE SSEOL', '썰')
    self.checkletter('HANGUL SYLLABLE YI', '의')
    self.checkletter('HANGUL SYLLABLE JJYOSS', '쭀')
    self.checkletter('HANGUL SYLLABLE KYEOLS', '켨')
    self.checkletter('HANGUL SYLLABLE PAN', '판')
    self.checkletter('HANGUL SYLLABLE HWEOK', '훸')
    self.checkletter('HANGUL SYLLABLE HIH', '힣')
    self.assertRaises(ValueError, unicodedata.name, '\ud7a4')
