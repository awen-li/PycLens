# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_send_at_certain_offset

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    total_sent = 0
    offset = len(self.DATA) // 2
    must_send = len(self.DATA) - offset
    nbytes = 4096
    while total_sent < must_send:
        sent = self.sendfile_wrapper(self.sockno, self.fileno, offset, nbytes)
        if sent == 0:
            break
        offset += sent
        total_sent += sent
        self.assertTrue(sent <= nbytes)
    self.client.shutdown(socket.SHUT_RDWR)
    self.client.close()
    self.server.wait()
    data = self.server.handler_instance.get_data()
    expected = self.DATA[len(self.DATA) // 2:]
    self.assertEqual(total_sent, len(expected))
    self.assertEqual(len(data), len(expected))
    self.assertEqual(data, expected)
