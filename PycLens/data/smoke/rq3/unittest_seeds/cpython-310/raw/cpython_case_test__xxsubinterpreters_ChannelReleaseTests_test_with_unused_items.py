# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelReleaseTests_test_with_unused_items

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, b'spam')
    interpreters.channel_send(cid, b'ham')
    interpreters.channel_release(cid, send=True, recv=True)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_recv(cid)
