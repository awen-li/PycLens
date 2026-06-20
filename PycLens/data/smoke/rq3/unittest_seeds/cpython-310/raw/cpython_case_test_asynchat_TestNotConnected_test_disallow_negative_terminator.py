# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestNotConnected_test_disallow_negative_terminator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    client = asynchat.async_chat()
    self.assertRaises(ValueError, client.set_terminator, -1)
