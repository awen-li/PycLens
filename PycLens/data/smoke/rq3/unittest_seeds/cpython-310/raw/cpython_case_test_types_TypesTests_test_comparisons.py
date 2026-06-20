# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_comparisons

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if 0 < 1 <= 1 == 1 >= 1 > 0 != 1:
        pass
    else:
        self.fail('int comparisons failed')
    if 0.0 < 1.0 <= 1.0 == 1.0 >= 1.0 > 0.0 != 1.0:
        pass
    else:
        self.fail('float comparisons failed')
    if '' < 'a' <= 'a' == 'a' < 'abc' < 'abd' < 'b':
        pass
    else:
        self.fail('string comparisons failed')
    if None is None:
        pass
    else:
        self.fail('identity test failed')
