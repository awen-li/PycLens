# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv2Tests_test_caps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    caps = self.server.getcapabilities()
    self.assertEqual(caps, {'VERSION': ['2', '3'], 'IMPLEMENTATION': ['INN', '2.5.1'], 'AUTHINFO': ['USER'], 'HDR': [], 'LIST': ['ACTIVE', 'ACTIVE.TIMES', 'DISTRIB.PATS', 'HEADERS', 'NEWSGROUPS', 'OVERVIEW.FMT'], 'OVER': [], 'POST': [], 'READER': []})
    self.assertEqual(self.server.nntp_version, 3)
    self.assertEqual(self.server.nntp_implementation, 'INN 2.5.1')
