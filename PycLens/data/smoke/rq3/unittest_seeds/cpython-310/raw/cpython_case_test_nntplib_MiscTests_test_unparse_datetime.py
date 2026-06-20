# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MiscTests_test_unparse_datetime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gives(y, M, d, h, m, s, date_str, time_str):
        dt = datetime.datetime(y, M, d, h, m, s)
        self.assertEqual(nntplib._unparse_datetime(dt), (date_str, time_str))
        self.assertEqual(nntplib._unparse_datetime(dt, False), (date_str, time_str))
    gives(1999, 6, 23, 13, 56, 24, '19990623', '135624')
    gives(2000, 6, 23, 13, 56, 24, '20000623', '135624')
    gives(2010, 6, 5, 1, 2, 3, '20100605', '010203')

    def gives(y, M, d, date_str, time_str):
        dt = datetime.date(y, M, d)
        self.assertEqual(nntplib._unparse_datetime(dt), (date_str, time_str))
        self.assertEqual(nntplib._unparse_datetime(dt, False), (date_str, time_str))
    gives(1999, 6, 23, '19990623', '000000')
    gives(2000, 6, 23, '20000623', '000000')
    gives(2010, 6, 5, '20100605', '000000')
