# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_boolean_ops

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if 0 or 0:
        self.fail('0 or 0 is true instead of false')
    if 1 and 1:
        pass
    else:
        self.fail('1 and 1 is false instead of true')
    if not 1:
        self.fail('not 1 is true instead of false')
