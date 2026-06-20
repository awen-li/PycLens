# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_re_groupref_exists_validation_bug

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for i in range(256):
        with self.subTest(code=i):
            re.compile('()(?(1)\\x%02x?)' % i)
