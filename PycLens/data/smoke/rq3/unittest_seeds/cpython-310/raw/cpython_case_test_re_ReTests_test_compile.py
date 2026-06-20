# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_compile

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern = re.compile('random pattern')
    self.assertIsInstance(pattern, re.Pattern)
    same_pattern = re.compile(pattern)
    self.assertIsInstance(same_pattern, re.Pattern)
    self.assertIs(same_pattern, pattern)
    self.assertRaises(TypeError, re.compile, 0)
