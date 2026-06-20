# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BufferingFormatterTest_test_custom

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = TestBufferingFormatter()
    self.assertEqual('[(2)onetwo(2)]', f.format(self.records))
    lf = logging.Formatter('<%(message)s>')
    f = TestBufferingFormatter(lf)
    self.assertEqual('[(2)<one><two>(2)]', f.format(self.records))
