# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_numeric_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if 0 != 0.0 or 1 != 1.0 or -1 != -1.0:
        self.fail('int/float value not equal')
    if int() != 0:
        self.fail('int() does not return 0')
    if float() != 0.0:
        self.fail('float() does not return 0.0')
    if int(1.9) == 1 == int(1.1) and int(-1.1) == -1 == int(-1.9):
        pass
    else:
        self.fail('int() does not round properly')
    if float(1) == 1.0 and float(-1) == -1.0 and (float(0) == 0.0):
        pass
    else:
        self.fail('float() does not work properly')
