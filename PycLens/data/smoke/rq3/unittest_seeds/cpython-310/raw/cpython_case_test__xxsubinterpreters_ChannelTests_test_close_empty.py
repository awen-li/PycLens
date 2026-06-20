# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_close_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    tests = [(False, False), (True, False), (False, True), (True, True)]
    for (send, recv) in tests:
        with self.subTest((send, recv)):
            cid = interpreters.channel_create()
            interpreters.channel_send(cid, b'spam')
            interpreters.channel_recv(cid)
            interpreters.channel_close(cid, send=send, recv=recv)
            with self.assertRaises(interpreters.ChannelClosedError):
                interpreters.channel_send(cid, b'eggs')
            with self.assertRaises(interpreters.ChannelClosedError):
                interpreters.channel_recv(cid)
