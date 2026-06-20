# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_floats

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if 12.0 + 24.0 != 36.0:
        self.fail('float op')
    if 12.0 + -24.0 != -12.0:
        self.fail('float op')
    if -12.0 + 24.0 != 12.0:
        self.fail('float op')
    if -12.0 + -24.0 != -36.0:
        self.fail('float op')
    if not 12.0 < 24.0:
        self.fail('float op')
    if not -24.0 < -12.0:
        self.fail('float op')
