# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_too_long_lines

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dt = datetime.datetime(2010, 1, 1, 9, 0, 0)
    self.assertRaises(nntplib.NNTPDataError, self.server.newnews, 'comp.lang.python', dt)
