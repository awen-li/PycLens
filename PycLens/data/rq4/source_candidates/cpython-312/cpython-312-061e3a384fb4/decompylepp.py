# Source Generated with Decompyle++
# File: cpython-312-061e3a384fb4.pyc (Python 3.12)


def __pybcsec_seed__():
    self = None(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, object)
    __pybcsec_self__ = None(None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, None, object)
    __pybcsec_self__ = self
    
    class AuthHandler(SimpleIMAPHandler):
        capabilities = 'LOGINDISABLED AUTH=CRAM-MD5'
        
        def cmd_AUTHENTICATE(self, tag, args):
            if None:
                pass
            self._send_textline('+ PDE4OTYuNjk3MTcwOTUyQHBvc3RvZmZpY2UucmVzdG9uLm1jaS5uZXQ=')
            if None:
                pass
            r = None
            if r == b'dGltIGYxY2E2YmU0NjRiOWVmYTFjY2E2ZmZkNmNmMmQ5ZjMy\r\n':
                self._send_tagged(tag, 'OK', 'CRAM-MD5 successful')
                return None
            self._send_tagged(tag, 'NO', 'No access')


    (client, _) = self._setup(AuthHandler)
    self.assertTrue('AUTH=CRAM-MD5' in client.capabilities)
    (ret, _) = client.login_cram_md5('tim', b'tanstaaftanstaaf')
    self.assertEqual(ret, 'OK')

if __name__ == '__main__':
    __pybcsec_seed__()
    return None
