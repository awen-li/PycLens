# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_search_disallows_charset_in_utf8_mode

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.reaped_pair(self.UTF8Server) as (server, client):
        (typ, _) = client.authenticate('MYAUTH', lambda x: b'fake')
        self.assertEqual(typ, 'OK')
        (typ, _) = client.enable('UTF8=ACCEPT')
        self.assertEqual(typ, 'OK')
        self.assertTrue(client.utf8_enabled)
        self.assertRaises(imaplib.IMAP4.error, client.search, 'foo', 'bar')
