# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_imaplib.py
# case: TestImaplib_test_imap4_host_default_value

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with socket.socket() as s:
        try:
            s.connect(('', imaplib.IMAP4_PORT))
            self.skipTest('Cannot run the test with local IMAP server running.')
        except socket.error:
            pass
    expected_errnos = socket_helper.get_socket_conn_refused_errs()
    with self.assertRaises(OSError) as cm:
        imaplib.IMAP4()
    self.assertIn(cm.exception.errno, expected_errnos)
