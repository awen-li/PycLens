# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_send_channel_does_not_exist

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ch = interpreters.SendChannel(1000000)
    with self.assertRaises(interpreters.ChannelNotFoundError):
        ch.send(b'spam')
