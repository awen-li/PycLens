# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_enable_raises_error_if_not_AUTH

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EnableHandler(SimpleIMAPHandler):
        capabilities = 'AUTH ENABLE UTF8=ACCEPT'
    (client, _) = self._setup(EnableHandler)
    self.assertFalse(client.utf8_enabled)
    with self.assertRaisesRegex(imaplib.IMAP4.error, 'ENABLE.*NONAUTH'):
        client.enable('foo')
    self.assertFalse(client.utf8_enabled)
