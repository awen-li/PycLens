# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_send_recv_different_interpreters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    cid = interpreters.channel_create()
    id1 = interpreters.create()
    out = _run_output(id1, dedent(f"\n            import _xxsubinterpreters as _interpreters\n            _interpreters.channel_send({cid}, b'spam')\n            "))
    obj = interpreters.channel_recv(cid)
    self.assertEqual(obj, b'spam')
