# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_difflib.py
# case: TestJunkAPIs_test_is_character_junk_true

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for char in [' ', '\t']:
        self.assertTrue(difflib.IS_CHARACTER_JUNK(char), repr(char))
