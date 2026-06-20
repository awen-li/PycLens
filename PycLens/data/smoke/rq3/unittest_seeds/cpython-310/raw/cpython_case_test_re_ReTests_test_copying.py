# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_copying

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import copy
    p = re.compile('(?P<int>\\d+)(?:\\.(?P<frac>\\d*))?')
    self.assertIs(copy.copy(p), p)
    self.assertIs(copy.deepcopy(p), p)
    m = p.match('12.34')
    self.assertIs(copy.copy(m), m)
    self.assertIs(copy.deepcopy(m), m)
