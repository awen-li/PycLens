# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_fstring.py
# case: TestCase_test_misformed_unicode_character_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertAllRaise(SyntaxError, "\\(unicode error\\) 'unicodeescape' codec can't decode bytes in position .*: malformed \\\\N character escape", ["f'\\N'", "f'\\N '", "f'\\N  '", "f'\\N{'", "f'\\N{GREEK CAPITAL LETTER DELTA'", "'\\N'", "'\\N '", "'\\N  '", "'\\N{'", "'\\N{GREEK CAPITAL LETTER DELTA'"])
