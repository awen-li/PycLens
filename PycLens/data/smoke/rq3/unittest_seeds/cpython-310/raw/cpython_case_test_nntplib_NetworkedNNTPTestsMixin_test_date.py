# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_date

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, date) = self.server.date()
    self.assertIsInstance(date, datetime.datetime)
    self.assertGreaterEqual(date.year, 1995)
    self.assertLessEqual(date.year, 2030)
