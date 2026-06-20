# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1v2TestsMixin_test_xover

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, overviews) = self.server.xover(57, 59)
    self.check_over_xover_resp(resp, overviews)
