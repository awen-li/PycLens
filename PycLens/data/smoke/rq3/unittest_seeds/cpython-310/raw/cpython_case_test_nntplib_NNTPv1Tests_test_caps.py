# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NNTPv1Tests_test_caps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    caps = self.server.getcapabilities()
    self.assertEqual(caps, {})
    self.assertEqual(self.server.nntp_version, 1)
    self.assertEqual(self.server.nntp_implementation, None)
