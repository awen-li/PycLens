# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestRecvChannelAttrs_test_id_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (rch, _) = interpreters.create_channel()
    self.assertIsInstance(rch.id, _interpreters.ChannelID)
