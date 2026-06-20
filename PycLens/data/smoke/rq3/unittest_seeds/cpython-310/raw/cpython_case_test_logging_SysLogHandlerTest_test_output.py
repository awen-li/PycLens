# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: SysLogHandlerTest_test_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if self.server_exception:
        self.skipTest(self.server_exception)
    logger = logging.getLogger('slh')
    logger.error('späm')
    self.handled.wait()
    self.assertEqual(self.log_output, b'<11>sp\xc3\xa4m\x00')
    self.handled.clear()
    self.sl_hdlr.append_nul = False
    logger.error('späm')
    self.handled.wait()
    self.assertEqual(self.log_output, b'<11>sp\xc3\xa4m')
    self.handled.clear()
    self.sl_hdlr.ident = 'häm-'
    logger.error('späm')
    self.handled.wait()
    self.assertEqual(self.log_output, b'<11>h\xc3\xa4m-sp\xc3\xa4m')
