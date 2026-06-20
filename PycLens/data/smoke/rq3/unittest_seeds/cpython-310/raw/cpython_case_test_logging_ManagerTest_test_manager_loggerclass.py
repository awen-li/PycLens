# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ManagerTest_test_manager_loggerclass

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logged = []

    class MyLogger(logging.Logger):

        def _log(self, level, msg, args, exc_info=None, extra=None):
            logged.append(msg)
    man = logging.Manager(None)
    self.assertRaises(TypeError, man.setLoggerClass, int)
    man.setLoggerClass(MyLogger)
    logger = man.getLogger('test')
    logger.warning('should appear in logged')
    logging.warning('should not appear in logged')
    self.assertEqual(logged, ['should appear in logged'])
