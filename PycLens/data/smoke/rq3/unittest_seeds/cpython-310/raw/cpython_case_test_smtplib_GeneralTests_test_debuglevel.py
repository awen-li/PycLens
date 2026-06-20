# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_smtplib.py
# case: GeneralTests_test_debuglevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mock_socket.reply_with(b'220 Hello world')
    client = self.client()
    client.set_debuglevel(1)
    with support.captured_stderr() as stderr:
        client.connect(HOST, self.port)
    client.close()
    expected = re.compile('^connect:', re.MULTILINE)
    self.assertRegex(stderr.getvalue(), expected)
