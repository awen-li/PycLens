# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_issue5949

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EOFHandler(socketserver.StreamRequestHandler):

        def handle(self):
            self.wfile.write(b'* OK')
    with self.reaped_server(EOFHandler) as server:
        self.assertRaises(imaplib.IMAP4.abort, self.imap_class, *server.server_address)
