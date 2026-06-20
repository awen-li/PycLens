# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_login

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client, _) = self._setup(SimpleIMAPHandler)
    (typ, data) = client.login('user', 'pass')
    self.assertEqual(typ, 'OK')
    self.assertEqual(data[0], b'LOGIN completed')
    self.assertEqual(client.state, 'AUTH')
