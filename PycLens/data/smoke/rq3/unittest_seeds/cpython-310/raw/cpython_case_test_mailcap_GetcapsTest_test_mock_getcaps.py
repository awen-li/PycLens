# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_mailcap.py
# case: GetcapsTest_test_mock_getcaps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with os_helper.EnvironmentVarGuard() as env:
        env['MAILCAPS'] = MAILCAPFILE
        caps = mailcap.getcaps()
        self.assertDictEqual(caps, MAILCAPDICT)
