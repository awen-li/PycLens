# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_search_disallows_charset_in_utf8_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class UTF8Server(SimpleIMAPHandler):
        capabilities = 'AUTH ENABLE UTF8=ACCEPT'

        def cmd_ENABLE(self, tag, args):
            self._send_tagged(tag, 'OK', 'ENABLE successful')

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+')
            self.server.response = (yield)
            self._send_tagged(tag, 'OK', 'FAKEAUTH successful')
    (client, _) = self._setup(UTF8Server)
    (typ, _) = client.authenticate('MYAUTH', lambda x: b'fake')
    self.assertEqual(typ, 'OK')
    (typ, _) = client.enable('UTF8=ACCEPT')
    self.assertEqual(typ, 'OK')
    self.assertTrue(client.utf8_enabled)
    with self.assertRaisesRegex(imaplib.IMAP4.error, 'charset.*UTF8'):
        client.search('foo', 'bar')
