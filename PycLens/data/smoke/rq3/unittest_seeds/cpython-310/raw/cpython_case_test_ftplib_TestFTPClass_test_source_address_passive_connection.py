# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ftplib.py
# case: TestFTPClass_test_source_address_passive_connection

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    port = socket_helper.find_unused_port()
    self.client.source_address = (HOST, port)
    try:
        with self.client.transfercmd('list') as sock:
            self.assertEqual(sock.getsockname()[1], port)
    except OSError as e:
        if e.errno == errno.EADDRINUSE:
            self.skipTest("couldn't bind to port %d" % port)
        raise
