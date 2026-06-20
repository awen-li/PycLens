# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: RETests_test_repr

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(repr(Pattern), 'typing.Pattern')
    self.assertEqual(repr(Pattern[str]), 'typing.Pattern[str]')
    self.assertEqual(repr(Pattern[bytes]), 'typing.Pattern[bytes]')
    self.assertEqual(repr(Match), 'typing.Match')
    self.assertEqual(repr(Match[str]), 'typing.Match[str]')
    self.assertEqual(repr(Match[bytes]), 'typing.Match[bytes]')
