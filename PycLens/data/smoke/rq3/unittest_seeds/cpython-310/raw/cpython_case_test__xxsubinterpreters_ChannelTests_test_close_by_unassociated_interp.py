# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_close_by_unassociated_interp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interpreters.channel_send(cid, b'spam')
    interp = interpreters.create()
    interpreters.run_string(interp, dedent(f'\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_close({cid}, force=True)\n            '))
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_recv(cid)
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_close(cid)
