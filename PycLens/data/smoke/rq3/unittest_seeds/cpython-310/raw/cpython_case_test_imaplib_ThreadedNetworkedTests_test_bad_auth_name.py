# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_bad_auth_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(SimpleIMAPHandler):

        def cmd_AUTHENTICATE(self, tag, args):
            self._send_tagged(tag, 'NO', 'unrecognized authentication type {}'.format(args[0]))
    with self.reaped_pair(MyServer) as (server, client):
        with self.assertRaises(imaplib.IMAP4.error):
            client.authenticate('METHOD', lambda : 1)
