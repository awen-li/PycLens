# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_last_modified

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    response = self.request(self.base_url + '/test')
    self.check_status_and_reason(response, HTTPStatus.OK, data=self.data)
    last_modif_header = response.headers['Last-modified']
    self.assertEqual(last_modif_header, self.last_modif_header)
