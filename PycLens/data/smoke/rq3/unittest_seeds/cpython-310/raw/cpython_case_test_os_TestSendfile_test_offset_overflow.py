# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_os.py
# case: TestSendfile_test_offset_overflow

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    offset = len(self.DATA) + 4096
    try:
        sent = os.sendfile(self.sockno, self.fileno, offset, 4096)
    except OSError as e:
        if e.errno != errno.EINVAL:
            raise
    else:
        self.assertEqual(sent, 0)
    self.client.shutdown(socket.SHUT_RDWR)
    self.client.close()
    self.server.wait()
    data = self.server.handler_instance.get_data()
    self.assertEqual(data, b'')
