# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: LogRecordFactoryTest_test_logrecord_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, self.root_logger.warning, self.next_message())
    logging.setLogRecordFactory(DerivedLogRecord)
    self.root_logger.error(self.next_message())
    self.assert_log_lines([('root', 'ERROR', '2')])
