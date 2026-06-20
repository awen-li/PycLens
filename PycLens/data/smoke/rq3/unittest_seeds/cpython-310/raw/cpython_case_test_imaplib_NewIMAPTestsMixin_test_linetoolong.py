# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_linetoolong

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TooLongHandler(SimpleIMAPHandler):

        def handle(self):
            self.wfile.write(b'* OK ' + 11 * b'x' + b'\r\n')
    (_, server) = self._setup(TooLongHandler, connect=False)
    with self.assertRaisesRegex(imaplib.IMAP4.error, 'got more than 10 bytes'):
        self.imap_class(*server.server_address)
