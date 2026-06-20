# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_send_not_found

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with self.assertRaises(interpreters.ChannelNotFoundError):
        interpreters.channel_send(10, b'spam')
