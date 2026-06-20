# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_send_recv_same_interpreter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    interp = interpreters.create()
    interp.run(dedent("\n            from test.support import interpreters\n            r, s = interpreters.create_channel()\n            orig = b'spam'\n            s.send_nowait(orig)\n            obj = r.recv()\n            assert obj == orig, 'expected: obj == orig'\n            assert obj is not orig, 'expected: obj is not orig'\n            "))
