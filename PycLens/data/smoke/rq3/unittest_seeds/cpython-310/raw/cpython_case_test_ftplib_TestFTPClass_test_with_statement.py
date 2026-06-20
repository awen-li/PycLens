# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_with_statement

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.quit()

    def is_client_connected():
        if self.client.sock is None:
            return False
        try:
            self.client.sendcmd('noop')
        except (OSError, EOFError):
            return False
        return True
    with ftplib.FTP(timeout=TIMEOUT) as self.client:
        self.client.connect(self.server.host, self.server.port)
        self.client.sendcmd('noop')
        self.assertTrue(is_client_connected())
    self.assertEqual(self.server.handler_instance.last_received_cmd, 'quit')
    self.assertFalse(is_client_connected())
    with ftplib.FTP(timeout=TIMEOUT) as self.client:
        self.client.connect(self.server.host, self.server.port)
        self.client.sendcmd('noop')
        self.client.quit()
    self.assertEqual(self.server.handler_instance.last_received_cmd, 'quit')
    self.assertFalse(is_client_connected())
    try:
        with ftplib.FTP(timeout=TIMEOUT) as self.client:
            self.client.connect(self.server.host, self.server.port)
            self.client.sendcmd('noop')
            self.server.handler_instance.next_response = '550 error on quit'
    except ftplib.error_perm as err:
        self.assertEqual(str(err), '550 error on quit')
    else:
        self.fail('Exception not raised')
    time.sleep(0.1)
    self.assertEqual(self.server.handler_instance.last_received_cmd, 'quit')
    self.assertFalse(is_client_connected())
