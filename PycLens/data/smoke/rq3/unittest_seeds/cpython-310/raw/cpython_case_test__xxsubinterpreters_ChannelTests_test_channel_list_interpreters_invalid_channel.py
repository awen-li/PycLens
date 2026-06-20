# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_channel_list_interpreters_invalid_channel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    with self.assertRaises(interpreters.ChannelNotFoundError):
        interpreters.channel_list_interpreters(1000, send=True)
    interpreters.channel_close(cid)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_list_interpreters(cid, send=True)
