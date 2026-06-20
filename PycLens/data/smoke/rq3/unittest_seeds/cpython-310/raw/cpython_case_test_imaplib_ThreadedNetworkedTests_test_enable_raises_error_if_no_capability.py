# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_enable_raises_error_if_no_capability

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class NoEnableServer(self.UTF8Server):
        capabilities = 'AUTH'
    with self.reaped_pair(NoEnableServer) as (server, client):
        self.assertRaises(imaplib.IMAP4.error, client.enable, 'foo')
