# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelReleaseTests_test_no_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, b'spam')
    interpreters.channel_recv(cid)
    interpreters.channel_release(cid)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_send(cid, b'eggs')
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_recv(cid)
