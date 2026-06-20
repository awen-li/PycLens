# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BufferingFormatterTest_test_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = logging.BufferingFormatter()
    self.assertEqual('', f.format([]))
    self.assertEqual('onetwo', f.format(self.records))
