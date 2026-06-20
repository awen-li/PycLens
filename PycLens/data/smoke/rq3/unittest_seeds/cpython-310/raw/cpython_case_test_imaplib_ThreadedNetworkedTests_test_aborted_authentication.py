# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_aborted_authentication

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(SimpleIMAPHandler):

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_textline('+')
            self.response = (yield)
            if self.response == b'*\r\n':
                self._send_tagged(tag, 'NO', '[AUTHENTICATIONFAILED] aborted')
            else:
                self._send_tagged(tag, 'OK', 'MYAUTH successful')
    with self.reaped_pair(MyServer) as (server, client):
        with self.assertRaises(imaplib.IMAP4.error):
            (code, data) = client.authenticate('MYAUTH', lambda x: None)
