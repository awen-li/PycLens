# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_login_cram_md5

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class AuthHandler(SimpleIMAPHandler):
        capabilities = 'LOGINDISABLED AUTH=CRAM-MD5'

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+ PDE4OTYuNjk3MTcwOTUyQHBvc3RvZmZpY2UucmVzdG9uLm1jaS5uZXQ=')
            r = (yield)
            if r == b'dGltIGYxY2E2YmU0NjRiOWVmYTFjY2E2ZmZkNmNmMmQ5ZjMy\r\n':
                self._send_tagged(tag, 'OK', 'CRAM-MD5 successful')
            else:
                self._send_tagged(tag, 'NO', 'No access')
    with self.reaped_pair(AuthHandler) as (server, client):
        self.assertTrue('AUTH=CRAM-MD5' in client.capabilities)
        (ret, data) = client.login_cram_md5('tim', 'tanstaaftanstaaf')
        self.assertEqual(ret, 'OK')
    with self.reaped_pair(AuthHandler) as (server, client):
        self.assertTrue('AUTH=CRAM-MD5' in client.capabilities)
        (ret, data) = client.login_cram_md5('tim', b'tanstaaftanstaaf')
        self.assertEqual(ret, 'OK')
