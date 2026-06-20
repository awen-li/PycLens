# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_recv_nowait_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (ch, _) = interpreters.create_channel()
    with self.assertRaises(interpreters.ChannelEmptyError):
        ch.recv_nowait()
