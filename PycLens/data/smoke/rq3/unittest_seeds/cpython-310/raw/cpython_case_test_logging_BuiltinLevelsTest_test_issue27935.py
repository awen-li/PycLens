# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BuiltinLevelsTest_test_issue27935

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fatal = logging.getLevelName('FATAL')
    self.assertEqual(fatal, logging.FATAL)
