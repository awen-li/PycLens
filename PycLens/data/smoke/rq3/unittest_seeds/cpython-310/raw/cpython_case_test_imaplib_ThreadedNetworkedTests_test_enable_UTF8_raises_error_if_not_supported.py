# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_enable_UTF8_raises_error_if_not_supported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NonUTF8Server(SimpleIMAPHandler):
        pass
    with self.assertRaises(imaplib.IMAP4.error):
        with self.reaped_pair(NonUTF8Server) as (server, client):
            (typ, data) = client.login('user', 'pass')
            self.assertEqual(typ, 'OK')
            client.enable('UTF8=ACCEPT')
            pass
