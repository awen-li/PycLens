# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_valid_authentication_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(SimpleIMAPHandler):

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+')
            self.server.response = (yield)
            self._send_tagged(tag, 'OK', 'FAKEAUTH successful')
    (client, server) = self._setup(MyServer)
    (code, _) = client.authenticate('MYAUTH', lambda x: b'fake')
    self.assertEqual(code, 'OK')
    self.assertEqual(server.response, b'ZmFrZQ==\r\n')
