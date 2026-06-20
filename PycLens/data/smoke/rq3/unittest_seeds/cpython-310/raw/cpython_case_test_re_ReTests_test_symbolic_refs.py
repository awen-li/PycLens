# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_symbolic_refs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.sub('(?P<a>x)|(?P<b>y)', '\\g<b>', 'xx'), '')
    self.assertEqual(re.sub('(?P<a>x)|(?P<b>y)', '\\2', 'xx'), '')
    self.assertEqual(re.sub(b'(?P<a1>x)', b'\\g<a1>', b'xx'), b'xx')
    self.assertEqual(re.sub('(?P<µ>x)', '\\g<µ>', 'xx'), 'xx')
    self.assertEqual(re.sub('(?P<𝔘𝔫𝔦𝔠𝔬𝔡𝔢>x)', '\\g<𝔘𝔫𝔦𝔠𝔬𝔡𝔢>', 'xx'), 'xx')
    pat = '|'.join(('x(?P<a%d>%x)y' % (i, i) for i in range(1, 200 + 1)))
    self.assertEqual(re.sub(pat, '\\g<200>', 'xc8yzxc8y'), 'c8zc8')
