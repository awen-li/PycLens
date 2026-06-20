# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelReleaseTests_test_partially

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, None)
    interpreters.channel_recv(cid)
    interpreters.channel_send(cid, b'spam')
    interpreters.channel_release(cid, send=True)
    obj = interpreters.channel_recv(cid)
    self.assertEqual(obj, b'spam')
