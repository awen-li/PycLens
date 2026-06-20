# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_with_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.reaped_server(SimpleIMAPHandler) as server:
        with self.imap_class(*server.server_address) as imap:
            imap.login('user', 'pass')
            self.assertEqual(server.logged, 'user')
        self.assertIsNone(server.logged)
