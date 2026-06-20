# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ModuleLevelMiscTest_test_set_logger_class

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, logging.setLoggerClass, object)

    class MyLogger(logging.Logger):
        pass
    logging.setLoggerClass(MyLogger)
    self.assertEqual(logging.getLoggerClass(), MyLogger)
    logging.setLoggerClass(logging.Logger)
    self.assertEqual(logging.getLoggerClass(), logging.Logger)
