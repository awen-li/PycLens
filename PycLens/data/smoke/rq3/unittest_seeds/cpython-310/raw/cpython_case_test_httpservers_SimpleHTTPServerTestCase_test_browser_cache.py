# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_browser_cache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    headers = email.message.Message()
    headers['If-Modified-Since'] = self.last_modif_header
    response = self.request(self.base_url + '/test', headers=headers)
    self.check_status_and_reason(response, HTTPStatus.NOT_MODIFIED)
    new_dt = self.last_modif_datetime + datetime.timedelta(hours=1)
    headers = email.message.Message()
    headers['If-Modified-Since'] = email.utils.format_datetime(new_dt, usegmt=True)
    response = self.request(self.base_url + '/test', headers=headers)
    self.check_status_and_reason(response, HTTPStatus.NOT_MODIFIED)
