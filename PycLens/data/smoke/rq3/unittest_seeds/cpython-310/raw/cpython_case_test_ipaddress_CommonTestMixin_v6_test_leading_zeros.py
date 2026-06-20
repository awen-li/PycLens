# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v6_test_leading_zeros

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertInstancesEqual('0000::0000', '::')
    self.assertInstancesEqual('000::c0a8:0001', '::c0a8:1')
