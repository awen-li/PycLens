# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test__xxsubinterpreters.py
# case: ChannelTests_test_send_recv_same_interpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    id1 = interpreters.create()
    out = _run_output(id1, dedent("\n            import _xxsubinterpreters as _interpreters\n            cid = _interpreters.channel_create()\n            orig = b'spam'\n            _interpreters.channel_send(cid, orig)\n            obj = _interpreters.channel_recv(cid)\n            assert obj is not orig\n            assert obj == orig\n            "))
