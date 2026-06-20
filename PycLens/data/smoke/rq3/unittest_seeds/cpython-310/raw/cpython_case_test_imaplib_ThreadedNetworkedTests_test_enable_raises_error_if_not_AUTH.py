# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_enable_raises_error_if_not_AUTH

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.reaped_pair(self.UTF8Server) as (server, client):
        self.assertFalse(client.utf8_enabled)
        self.assertRaises(imaplib.IMAP4.error, client.enable, 'foo')
        self.assertFalse(client.utf8_enabled)
