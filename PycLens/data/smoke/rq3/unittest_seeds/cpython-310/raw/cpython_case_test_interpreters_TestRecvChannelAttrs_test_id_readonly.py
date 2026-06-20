# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestRecvChannelAttrs_test_id_readonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    rch = interpreters.RecvChannel(1)
    with self.assertRaises(AttributeError):
        rch.id = 2
