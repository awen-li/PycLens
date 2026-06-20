# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: MiscTests_test_parse_datetime

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gives(a, b, *c):
        self.assertEqual(nntplib._parse_datetime(a, b), datetime.datetime(*c))
    gives('19990623135624', None, 1999, 6, 23, 13, 56, 24)
    gives('19990623', '135624', 1999, 6, 23, 13, 56, 24)
    gives('990623', '135624', 1999, 6, 23, 13, 56, 24)
    gives('090623', '135624', 2009, 6, 23, 13, 56, 24)
