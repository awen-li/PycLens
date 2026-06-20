# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_issue18183

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    '𐀀\U00100000'.lower()
    '𐀀\U00100000'.casefold()
    '𐀀\U00100000'.upper()
    '𐀀\U00100000'.capitalize()
    '𐀀\U00100000'.title()
    '𐀀\U00100000'.swapcase()
    '\U00100000'.center(3, '𐀀')
    '\U00100000'.ljust(3, '𐀀')
    '\U00100000'.rjust(3, '𐀀')
