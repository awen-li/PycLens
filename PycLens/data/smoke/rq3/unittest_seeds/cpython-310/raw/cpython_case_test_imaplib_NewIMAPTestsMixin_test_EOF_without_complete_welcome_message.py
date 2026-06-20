# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: NewIMAPTestsMixin_test_EOF_without_complete_welcome_message

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class EOFHandler(socketserver.StreamRequestHandler):

        def handle(self):
            self.wfile.write(b'* OK')
    (_, server) = self._setup(EOFHandler, connect=False)
    self.assertRaises(imaplib.IMAP4.abort, self.imap_class, *server.server_address)
