# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_head

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    response = self.request(self.base_url + '/test', method='HEAD')
    self.check_status_and_reason(response, HTTPStatus.OK)
    self.assertEqual(response.getheader('content-length'), str(len(self.data)))
    self.assertEqual(response.getheader('content-type'), 'application/octet-stream')
