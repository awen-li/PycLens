# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: BasicFilterTest_test_empty_filter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    f = logging.Filter()
    r = logging.makeLogRecord({'name': 'spam.eggs'})
    self.assertTrue(f.filter(r))
