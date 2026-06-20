# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_invalid_requests

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    response = self.request('/', method='FOO')
    self.check_status_and_reason(response, HTTPStatus.NOT_IMPLEMENTED)
    response = self.request('/', method='custom')
    self.check_status_and_reason(response, HTTPStatus.NOT_IMPLEMENTED)
    response = self.request('/', method='GETs')
    self.check_status_and_reason(response, HTTPStatus.NOT_IMPLEMENTED)
