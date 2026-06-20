# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicConfigTest_test_format

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logging.basicConfig(format='%(asctime)s - %(message)s')
    formatter = logging.root.handlers[0].formatter
    self.assertEqual(formatter._style._fmt, '%(asctime)s - %(message)s')
