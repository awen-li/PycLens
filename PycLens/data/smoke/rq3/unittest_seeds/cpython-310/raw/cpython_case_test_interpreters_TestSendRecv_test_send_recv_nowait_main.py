# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_send_recv_nowait_main

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, s) = interpreters.create_channel()
    orig = b'spam'
    s.send_nowait(orig)
    obj = r.recv_nowait()
    self.assertEqual(obj, orig)
    self.assertIsNot(obj, orig)
