# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_imaplib_timeout_functionality_test

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TimeoutHandler(SimpleIMAPHandler):

        def handle(self):
            time.sleep(1)
            SimpleIMAPHandler.handle(self)
    (_, server) = self._setup(TimeoutHandler)
    addr = server.server_address[1]
    with self.assertRaises(TimeoutError):
        client = self.imap_class('localhost', addr, timeout=0.001)
