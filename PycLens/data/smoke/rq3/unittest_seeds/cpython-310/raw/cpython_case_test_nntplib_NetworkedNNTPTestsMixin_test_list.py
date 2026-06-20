# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_list

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (resp, groups) = self.server.list()
    if len(groups) > 0:
        self.assertEqual(GroupInfo, type(groups[0]))
        self.assertEqual(str, type(groups[0].group))
