# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_uuid.py
# case: BaseTestInternals_test_netstat_getnode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    node = self.uuid._netstat_getnode()
    self.check_node(node, 'netstat')
