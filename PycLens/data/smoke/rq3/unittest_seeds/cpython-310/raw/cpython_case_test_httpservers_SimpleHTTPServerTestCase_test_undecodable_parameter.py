# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_undecodable_parameter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    response = self.request(self.base_url + '/?x=123').read()
    self.assertRegex(response, f'listing for {self.base_url}/\\?x=123'.encode('latin1'))
    response = self.request(self.base_url + '/?x=%bb').read()
    self.assertRegex(response, f'listing for {self.base_url}/\\?x=ï¿½'.encode('latin1'))
