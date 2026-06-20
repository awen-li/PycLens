# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ModuleLevelMiscTest_test_subclass_logger_cache

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    message = []

    class MyLogger(logging.getLoggerClass()):

        def __init__(self, name='MyLogger', level=logging.NOTSET):
            super().__init__(name, level)
            message.append('initialized')
    logging.setLoggerClass(MyLogger)
    logger = logging.getLogger('just_some_logger')
    self.assertEqual(message, ['initialized'])
    stream = io.StringIO()
    h = logging.StreamHandler(stream)
    logger.addHandler(h)
    try:
        logger.setLevel(logging.DEBUG)
        logger.debug('hello')
        self.assertEqual(stream.getvalue().strip(), 'hello')
        stream.truncate(0)
        stream.seek(0)
        logger.setLevel(logging.INFO)
        logger.debug('hello')
        self.assertEqual(stream.getvalue(), '')
    finally:
        logger.removeHandler(h)
        h.close()
        logging.setLoggerClass(logging.Logger)
