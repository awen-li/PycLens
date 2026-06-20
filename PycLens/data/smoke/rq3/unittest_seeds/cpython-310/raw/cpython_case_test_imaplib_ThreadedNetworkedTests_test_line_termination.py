# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: ThreadedNetworkedTests_test_line_termination

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class BadNewlineHandler(SimpleIMAPHandler):

        def cmd_CAPABILITY(self, tag, args):
            self._send(b'* CAPABILITY IMAP4rev1 AUTH\n')
            self._send_tagged(tag, 'OK', 'CAPABILITY completed')
    with self.reaped_server(BadNewlineHandler) as server:
        self.assertRaises(imaplib.IMAP4.abort, self.imap_class, *server.server_address)
