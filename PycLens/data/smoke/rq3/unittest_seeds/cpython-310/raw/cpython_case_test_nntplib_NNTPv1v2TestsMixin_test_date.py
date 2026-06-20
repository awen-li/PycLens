# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_date

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, date) = self.server.date()
    self.assertEqual(resp, '111 20100914001155')
    self.assertEqual(date, datetime.datetime(2010, 9, 14, 0, 11, 55))
