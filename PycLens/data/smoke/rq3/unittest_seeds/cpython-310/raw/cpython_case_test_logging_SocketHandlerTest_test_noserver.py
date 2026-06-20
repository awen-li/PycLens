# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: SocketHandlerTest_test_noserver

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.server_exception:
        self.skipTest(self.server_exception)
    self.sock_hdlr.retryStart = 2.5
    self.server.stop()
    try:
        raise RuntimeError('Deliberate mistake')
    except RuntimeError:
        self.root_logger.exception('Never sent')
    self.root_logger.error('Never sent, either')
    now = time.time()
    self.assertGreater(self.sock_hdlr.retryTime, now)
    time.sleep(self.sock_hdlr.retryTime - now + 0.001)
    self.root_logger.error('Nor this')
