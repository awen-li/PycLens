# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_weakref

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    s = 'QabbbcR'
    x = re.compile('ab+c')
    y = proxy(x)
    self.assertEqual(x.findall('QabbbcR'), y.findall('QabbbcR'))
