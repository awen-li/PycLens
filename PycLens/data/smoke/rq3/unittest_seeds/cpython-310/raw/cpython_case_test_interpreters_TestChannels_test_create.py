# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestChannels_test_create

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, s) = interpreters.create_channel()
    self.assertIsInstance(r, interpreters.RecvChannel)
    self.assertIsInstance(s, interpreters.SendChannel)
