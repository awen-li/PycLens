# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_stack_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.match('(x)*', 50000 * 'x').group(1), 'x')
    self.assertEqual(re.match('(x)*y', 50000 * 'x' + 'y').group(1), 'x')
    self.assertEqual(re.match('(x)*?y', 50000 * 'x' + 'y').group(1), 'x')
