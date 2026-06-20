# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_statistics.py
# case: UnivariateCommonMixin_test_bad_arg_types

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.check_for_type_error(None)
    self.check_for_type_error(23)
    self.check_for_type_error(42.0)
    self.check_for_type_error(object())
