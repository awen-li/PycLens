# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_send_whole_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    total_sent = 0
    offset = 0
    nbytes = 4096
    while total_sent < len(self.DATA):
        sent = self.sendfile_wrapper(self.sockno, self.fileno, offset, nbytes)
        if sent == 0:
            break
        offset += sent
        total_sent += sent
        self.assertTrue(sent <= nbytes)
        self.assertEqual(offset, total_sent)
    self.assertEqual(total_sent, len(self.DATA))
    self.client.shutdown(socket.SHUT_RDWR)
    self.client.close()
    self.server.wait()
    data = self.server.handler_instance.get_data()
    self.assertEqual(len(data), len(self.DATA))
    self.assertEqual(data, self.DATA)
