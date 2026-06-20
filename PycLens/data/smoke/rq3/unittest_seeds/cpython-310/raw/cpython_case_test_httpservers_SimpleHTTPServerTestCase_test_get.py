# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: SimpleHTTPServerTestCase_test_get

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    response = self.request(self.base_url + '/test')
    self.check_status_and_reason(response, HTTPStatus.OK, data=self.data)
    response = self.request(self.base_url + '/test/')
    self.check_status_and_reason(response, HTTPStatus.NOT_FOUND)
    response = self.request(self.base_url + '/')
    self.check_status_and_reason(response, HTTPStatus.OK)
    response = self.request(self.base_url)
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    self.assertEqual(response.getheader('Content-Length'), '0')
    response = self.request(self.base_url + '/?hi=2')
    self.check_status_and_reason(response, HTTPStatus.OK)
    response = self.request(self.base_url + '?hi=1')
    self.check_status_and_reason(response, HTTPStatus.MOVED_PERMANENTLY)
    self.assertEqual(response.getheader('Location'), self.base_url + '/?hi=1')
    response = self.request('/ThisDoesNotExist')
    self.check_status_and_reason(response, HTTPStatus.NOT_FOUND)
    response = self.request('/' + 'ThisDoesNotExist' + '/')
    self.check_status_and_reason(response, HTTPStatus.NOT_FOUND)
    os.makedirs(os.path.join(self.tempdir, 'spam', 'index.html'))
    response = self.request(self.base_url + '/spam/')
    self.check_status_and_reason(response, HTTPStatus.OK)
    data = b'Dummy index file\r\n'
    with open(os.path.join(self.tempdir_name, 'index.html'), 'wb') as f:
        f.write(data)
    response = self.request(self.base_url + '/')
    self.check_status_and_reason(response, HTTPStatus.OK, data)
    if os.name == 'posix' and os.geteuid() != 0:
        os.chmod(self.tempdir, 0)
        try:
            response = self.request(self.base_url + '/')
            self.check_status_and_reason(response, HTTPStatus.NOT_FOUND)
        finally:
            os.chmod(self.tempdir, 493)
