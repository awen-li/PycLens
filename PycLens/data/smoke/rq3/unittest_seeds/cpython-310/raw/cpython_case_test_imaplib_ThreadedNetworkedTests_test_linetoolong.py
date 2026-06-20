# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_linetoolong

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class TooLongHandler(SimpleIMAPHandler):

        def handle(self):
            self.wfile.write(b'* OK ' + imaplib._MAXLINE * b'x' + b'\r\n')
    with self.reaped_server(TooLongHandler) as server:
        self.assertRaises(imaplib.IMAP4.error, self.imap_class, *server.server_address)
