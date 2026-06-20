# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_close_recv_with_unused_items_unforced

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, b'spam')
    interpreters.channel_send(cid, b'ham')
    with self.assertRaises(interpreters.ChannelNotEmptyError):
        interpreters.channel_close(cid, recv=True)
    interpreters.channel_recv(cid)
    interpreters.channel_send(cid, b'eggs')
    interpreters.channel_recv(cid)
    interpreters.channel_recv(cid)
    interpreters.channel_close(cid, recv=True)
