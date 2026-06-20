# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_path_without_leading_slash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    response = self.request(self.tempdir_name + '/test')
    self.check_status_and_reason(response, HTTPStatus.OK, data=self.data)
    response = self.request(self.tempdir_name + '/test/')
    self.check_status_and_reason(response, HTTPStatus.NOT_FOUND)
    response = self.request(self.tempdir_name + '/')
    self.check_status_and_reason(response, HTTPStatus.OK)
    response = self.request(self.tempdir_name)
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    response = self.request(self.tempdir_name + '/?hi=2')
    self.check_status_and_reason(response, HTTPStatus.OK)
    response = self.request(self.tempdir_name + '?hi=1')
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    self.assertEqual(response.getheader('Location'), self.tempdir_name + '/?hi=1')
