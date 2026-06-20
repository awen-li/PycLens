# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_1661

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pattern = re.compile('.')
    self.assertRaises(ValueError, re.match, pattern, 'A', re.I)
    self.assertRaises(ValueError, re.search, pattern, 'A', re.I)
    self.assertRaises(ValueError, re.findall, pattern, 'A', re.I)
    self.assertRaises(ValueError, re.compile, pattern, re.I)
