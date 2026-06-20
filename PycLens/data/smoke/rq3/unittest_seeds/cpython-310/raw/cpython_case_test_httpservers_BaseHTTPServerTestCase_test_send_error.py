# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPServerTestCase_test_send_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    allow_transfer_encoding_codes = (HTTPStatus.NOT_MODIFIED, HTTPStatus.RESET_CONTENT)
    for code in (HTTPStatus.NO_CONTENT, HTTPStatus.NOT_MODIFIED, HTTPStatus.PROCESSING, HTTPStatus.RESET_CONTENT, HTTPStatus.SWITCHING_PROTOCOLS):
        self.con.request('SEND_ERROR', '/{}'.format(code))
        res = self.con.getresponse()
        self.assertEqual(code, res.status)
        self.assertEqual(None, res.getheader('Content-Length'))
        self.assertEqual(None, res.getheader('Content-Type'))
        if code not in allow_transfer_encoding_codes:
            self.assertEqual(None, res.getheader('Transfer-Encoding'))
        data = res.read()
        self.assertEqual(b'', data)
