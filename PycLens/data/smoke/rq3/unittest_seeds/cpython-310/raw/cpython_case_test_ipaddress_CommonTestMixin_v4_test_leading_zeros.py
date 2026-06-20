# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ipaddress.py
# case: CommonTestMixin_v4_test_leading_zeros

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = "Leading zeros are not permitted in '\\d+'"
    addresses = ['000.000.000.000', '192.168.000.001', '016.016.016.016', '192.168.000.001', '001.000.008.016', '01.2.3.40', '1.02.3.40', '1.2.03.40', '1.2.3.040']
    for address in addresses:
        with self.subTest(address=address):
            with self.assertAddressError(msg):
                self.factory(address)
