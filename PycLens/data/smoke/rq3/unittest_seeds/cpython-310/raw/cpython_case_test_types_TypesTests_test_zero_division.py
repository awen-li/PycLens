# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_zero_division

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        5.0 / 0.0
    except ZeroDivisionError:
        pass
    else:
        self.fail("5.0 / 0.0 didn't raise ZeroDivisionError")
    try:
        5.0 // 0.0
    except ZeroDivisionError:
        pass
    else:
        self.fail("5.0 // 0.0 didn't raise ZeroDivisionError")
    try:
        5.0 % 0.0
    except ZeroDivisionError:
        pass
    else:
        self.fail("5.0 % 0.0 didn't raise ZeroDivisionError")
    try:
        5 / 0
    except ZeroDivisionError:
        pass
    else:
        self.fail("5 / 0 didn't raise ZeroDivisionError")
    try:
        5 // 0
    except ZeroDivisionError:
        pass
    else:
        self.fail("5 // 0 didn't raise ZeroDivisionError")
    try:
        5 % 0
    except ZeroDivisionError:
        pass
    else:
        self.fail("5 % 0 didn't raise ZeroDivisionError")
