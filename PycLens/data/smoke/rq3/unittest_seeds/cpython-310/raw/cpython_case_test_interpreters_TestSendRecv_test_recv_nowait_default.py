# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_recv_nowait_default

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    default = object()
    (rch, sch) = interpreters.create_channel()
    obj1 = rch.recv_nowait(default)
    sch.send_nowait(None)
    sch.send_nowait(1)
    sch.send_nowait(b'spam')
    sch.send_nowait(b'eggs')
    obj2 = rch.recv_nowait(default)
    obj3 = rch.recv_nowait(default)
    obj4 = rch.recv_nowait()
    obj5 = rch.recv_nowait(default)
    obj6 = rch.recv_nowait(default)
    self.assertIs(obj1, default)
    self.assertIs(obj2, None)
    self.assertEqual(obj3, 1)
    self.assertEqual(obj4, b'spam')
    self.assertEqual(obj5, b'eggs')
    self.assertIs(obj6, default)
