# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_headers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    total_sent = 0
    expected_data = b'x' * 512 + b'y' * 256 + self.DATA[:-1]
    sent = os.sendfile(self.sockno, self.fileno, 0, 4096, headers=[b'x' * 512, b'y' * 256])
    self.assertLessEqual(sent, 512 + 256 + 4096)
    total_sent += sent
    offset = 4096
    while total_sent < len(expected_data):
        nbytes = min(len(expected_data) - total_sent, 4096)
        sent = self.sendfile_wrapper(self.sockno, self.fileno, offset, nbytes)
        if sent == 0:
            break
        self.assertLessEqual(sent, nbytes)
        total_sent += sent
        offset += sent
    self.assertEqual(total_sent, len(expected_data))
    self.client.close()
    self.server.wait()
    data = self.server.handler_instance.get_data()
    self.assertEqual(hash(data), hash(expected_data))
