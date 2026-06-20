# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: ManagerTest_test_set_log_record_factory

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    man = logging.Manager(None)
    expected = object()
    man.setLogRecordFactory(expected)
    self.assertEqual(man.logRecordFactory, expected)
