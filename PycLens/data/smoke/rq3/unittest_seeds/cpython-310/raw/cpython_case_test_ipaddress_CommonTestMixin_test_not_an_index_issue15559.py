# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_test_not_an_index_issue15559

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, operator.index, self.factory(1))
    self.assertRaises(TypeError, hex, self.factory(1))
    self.assertRaises(TypeError, bytes, self.factory(1))
