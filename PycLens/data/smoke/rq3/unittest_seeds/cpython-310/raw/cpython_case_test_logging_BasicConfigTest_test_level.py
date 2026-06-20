# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_level

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    old_level = logging.root.level
    self.addCleanup(logging.root.setLevel, old_level)
    logging.basicConfig(level=57)
    self.assertEqual(logging.root.level, 57)
    logging.basicConfig(level=58)
    self.assertEqual(logging.root.level, 57)
