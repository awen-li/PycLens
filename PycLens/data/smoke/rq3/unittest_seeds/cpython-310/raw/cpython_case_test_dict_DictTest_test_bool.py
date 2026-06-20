# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dict.py
# case: DictTest_test_bool

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIs(not {}, True)
    self.assertTrue({1: 2})
    self.assertIs(bool({}), False)
    self.assertIs(bool({1: 2}), True)
