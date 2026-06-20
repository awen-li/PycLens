# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_locale.py
# case: TestMiscellaneous_test_strcoll_3303

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, locale.strcoll, 'a', None)
    self.assertRaises(TypeError, locale.strcoll, b'a', None)
