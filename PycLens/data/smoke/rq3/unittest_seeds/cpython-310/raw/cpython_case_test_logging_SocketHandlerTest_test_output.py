# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: SocketHandlerTest_test_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.server_exception:
        self.skipTest(self.server_exception)
    logger = logging.getLogger('tcp')
    logger.error('spam')
    self.handled.acquire()
    logger.debug('eggs')
    self.handled.acquire()
    self.assertEqual(self.log_output, 'spam\neggs\n')
