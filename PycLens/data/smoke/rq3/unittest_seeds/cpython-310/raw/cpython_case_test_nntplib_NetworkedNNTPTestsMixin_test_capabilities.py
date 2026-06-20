# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_nntplib.py
# case: NetworkedNNTPTestsMixin_test_capabilities

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def _check_caps(caps):
        caps_list = caps['LIST']
        self.assertIsInstance(caps_list, (list, tuple))
        self.assertIn('OVERVIEW.FMT', caps_list)
    self.assertGreaterEqual(self.server.nntp_version, 2)
    _check_caps(self.server.getcapabilities())
    (resp, caps) = self.server.capabilities()
    _check_caps(caps)
