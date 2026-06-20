# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_enable_UTF8_raises_error_if_not_supported

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client, _) = self._setup(SimpleIMAPHandler)
    (typ, data) = client.login('user', 'pass')
    self.assertEqual(typ, 'OK')
    with self.assertRaisesRegex(imaplib.IMAP4.error, 'does not support ENABLE'):
        client.enable('UTF8=ACCEPT')
