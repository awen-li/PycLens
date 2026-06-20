# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_newgroups

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    dt = datetime.date.today() - datetime.timedelta(days=7)
    (resp, groups) = self.server.newgroups(dt)
    if len(groups) > 0:
        self.assertIsInstance(groups[0], GroupInfo)
        self.assertIsInstance(groups[0].group, str)
