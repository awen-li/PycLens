# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BuiltinLevelsTest_test_regression_29220

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logging.addLevelName(logging.INFO, '')
    self.addCleanup(logging.addLevelName, logging.INFO, 'INFO')
    self.assertEqual(logging.getLevelName(logging.INFO), '')
    self.assertEqual(logging.getLevelName(logging.NOTSET), 'NOTSET')
    self.assertEqual(logging.getLevelName('NOTSET'), logging.NOTSET)
