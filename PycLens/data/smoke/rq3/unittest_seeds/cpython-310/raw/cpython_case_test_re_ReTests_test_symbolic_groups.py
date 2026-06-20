# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_symbolic_groups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    re.compile('(?P<a>x)(?P=a)(?(a)y)')
    re.compile('(?P<a1>x)(?P=a1)(?(a1)y)')
    re.compile('(?P<a1>x)\\1(?(1)y)')
    re.compile(b'(?P<a1>x)(?P=a1)(?(a1)y)')
    re.compile('(?P<µ>x)(?P=µ)(?(µ)y)')
    re.compile('(?P<𝔘𝔫𝔦𝔠𝔬𝔡𝔢>x)(?P=𝔘𝔫𝔦𝔠𝔬𝔡𝔢)(?(𝔘𝔫𝔦𝔠𝔬𝔡𝔢)y)')
    pat = '|'.join(('x(?P<a%d>%x)y' % (i, i) for i in range(1, 200 + 1)))
    pat = '(?:%s)(?(200)z|t)' % pat
    self.assertEqual(re.match(pat, 'xc8yz').span(), (0, 5))
