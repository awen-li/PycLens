# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: DatagramHandlerTest_test_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.server_exception:
        self.skipTest(self.server_exception)
    logger = logging.getLogger('udp')
    logger.error('spam')
    self.handled.wait()
    self.handled.clear()
    logger.error('eggs')
    self.handled.wait()
    self.assertEqual(self.log_output, 'spam\neggs\n')
