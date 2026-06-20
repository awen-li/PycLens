# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: NetworkedTests_test_get_server_certificate_ipv6

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket_helper.transient_internet('ipv6.google.com'):
        _test_get_server_certificate(self, 'ipv6.google.com', 443)
        _test_get_server_certificate_fail(self, 'ipv6.google.com', 443)
