# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_enable_UTF8_True_append

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UTF8AppendServer(SimpleIMAPHandler):
        capabilities = 'ENABLE UTF8=ACCEPT'

        def cmd_ENABLE(self, tag, args):
            self._send_tagged(tag, 'OK', 'ENABLE successful')

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+')
            self.server.response = (yield)
            self._send_tagged(tag, 'OK', 'FAKEAUTH successful')

        def cmd_APPEND(self, tag, args):
            self._send_textline('+')
            self.server.response = (yield)
            self._send_tagged(tag, 'OK', 'okay')
    (client, server) = self._setup(UTF8AppendServer)
    self.assertEqual(client._encoding, 'ascii')
    (code, _) = client.authenticate('MYAUTH', lambda x: b'fake')
    self.assertEqual(code, 'OK')
    self.assertEqual(server.response, b'ZmFrZQ==\r\n')
    (code, _) = client.enable('UTF8=ACCEPT')
    self.assertEqual(code, 'OK')
    self.assertEqual(client._encoding, 'utf-8')
    msg_string = 'Subject: üñí©öðé'
    (typ, data) = client.append(None, None, None, msg_string.encode('utf-8'))
    self.assertEqual(typ, 'OK')
    self.assertEqual(server.response, ('UTF8 (%s)\r\n' % msg_string).encode('utf-8'))
