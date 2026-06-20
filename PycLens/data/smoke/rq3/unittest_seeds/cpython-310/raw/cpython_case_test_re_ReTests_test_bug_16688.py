# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_bug_16688

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.findall('(?i)(a)\\1', 'aa Ā'), ['a'])
    self.assertEqual(re.match('(?s).{1,3}', 'ĀĀ').span(), (0, 2))
