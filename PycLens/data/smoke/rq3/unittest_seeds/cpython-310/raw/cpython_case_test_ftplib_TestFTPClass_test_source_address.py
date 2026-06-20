# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_source_address

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.client.quit()
    port = socket_helper.find_unused_port()
    try:
        self.client.connect(self.server.host, self.server.port, source_address=(HOST, port))
        self.assertEqual(self.client.sock.getsockname()[1], port)
        self.client.quit()
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            self.skipTest("couldn't bind to port %d" % port)
        raise
