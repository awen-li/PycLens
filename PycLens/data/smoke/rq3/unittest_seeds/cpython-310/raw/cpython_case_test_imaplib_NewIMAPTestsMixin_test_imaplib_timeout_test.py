# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_imaplib_timeout_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (_, server) = self._setup(SimpleIMAPHandler)
    addr = server.server_address[1]
    client = self.imap_class('localhost', addr, timeout=None)
    self.assertEqual(client.sock.timeout, None)
    client.shutdown()
    client = self.imap_class('localhost', addr, timeout=support.LOOPBACK_TIMEOUT)
    self.assertEqual(client.sock.timeout, support.LOOPBACK_TIMEOUT)
    client.shutdown()
    with self.assertRaises(ValueError):
        client = self.imap_class('localhost', addr, timeout=0)
