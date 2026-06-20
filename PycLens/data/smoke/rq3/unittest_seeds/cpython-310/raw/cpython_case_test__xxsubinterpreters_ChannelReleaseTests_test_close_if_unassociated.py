# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelReleaseTests_test_close_if_unassociated

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    interp = interpreters.create()
    interpreters.run_string(interp, dedent(f"\n            import _xxsubinterpreters as _interpreters\n            obj = _interpreters.channel_send({cid}, b'spam')\n            _interpreters.channel_release({cid})\n            "))
    with self.assertRaises(interpreters.ChannelClosedError):
        interpreters.channel_recv(cid)
