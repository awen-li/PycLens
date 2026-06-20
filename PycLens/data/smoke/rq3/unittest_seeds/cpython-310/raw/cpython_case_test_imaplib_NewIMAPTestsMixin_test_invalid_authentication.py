# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_invalid_authentication

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(SimpleIMAPHandler):

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+')
            self.response = (yield)
            self._send_tagged(tag, 'NO', '[AUTHENTICATIONFAILED] invalid')
    (client, _) = self._setup(MyServer)
    with self.assertRaisesRegex(imaplib.IMAP4.error, '\\[AUTHENTICATIONFAILED\\] invalid'):
        client.authenticate('MYAUTH', lambda x: b'fake')
