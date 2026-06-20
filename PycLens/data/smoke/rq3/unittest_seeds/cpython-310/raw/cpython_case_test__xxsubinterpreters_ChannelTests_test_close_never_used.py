# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_close_never_used

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interpreters.channel_close(cid)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_send(cid, b'spam')
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_recv(cid)
