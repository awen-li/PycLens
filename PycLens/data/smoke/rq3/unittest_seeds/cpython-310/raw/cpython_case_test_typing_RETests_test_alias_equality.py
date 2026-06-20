# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_typing.py
# case: RETests_test_alias_equality

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(Pattern[str], Pattern[str])
    self.assertNotEqual(Pattern[str], Pattern[bytes])
    self.assertNotEqual(Pattern[str], Match[str])
    self.assertNotEqual(Pattern[str], str)
