# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: RETests_test_basics

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pat = re.compile('[a-z]+', re.I)
    self.assertIsSubclass(pat.__class__, Pattern)
    self.assertIsSubclass(type(pat), Pattern)
    self.assertIsInstance(pat, Pattern)
    mat = pat.search('12345abcde.....')
    self.assertIsSubclass(mat.__class__, Match)
    self.assertIsSubclass(type(mat), Match)
    self.assertIsInstance(mat, Match)
    Pattern[Union[str, bytes]]
    Match[Union[bytes, str]]
