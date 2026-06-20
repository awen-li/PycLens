# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_unselect

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client, _) = self._setup(SimpleIMAPHandler)
    client.login('user', 'pass')
    (typ, data) = client.select()
    self.assertEqual(typ, 'OK')
    self.assertEqual(data[0], b'2')
    (typ, data) = client.unselect()
    self.assertEqual(typ, 'OK')
    self.assertEqual(data[0], b'Returned to authenticated state. (Success)')
    self.assertEqual(client.state, 'AUTH')
