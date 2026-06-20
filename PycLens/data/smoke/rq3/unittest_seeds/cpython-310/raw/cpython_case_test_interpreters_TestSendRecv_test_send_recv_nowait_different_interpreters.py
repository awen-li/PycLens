# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_send_recv_nowait_different_interpreters

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r1, s1) = interpreters.create_channel()
    (r2, s2) = interpreters.create_channel()
    orig1 = b'spam'
    s1.send_nowait(orig1)
    out = _run_output(interpreters.create(), dedent(f"\n                obj1 = r.recv_nowait()\n                assert obj1 == b'spam', 'expected: obj1 == orig1'\n                # When going to another interpreter we get a copy.\n                assert id(obj1) != {id(orig1)}, 'expected: obj1 is not orig1'\n                orig2 = b'eggs'\n                print(id(orig2))\n                s.send_nowait(orig2)\n                "), channels=dict(r=r1, s=s2))
    obj2 = r2.recv_nowait()
    self.assertEqual(obj2, b'eggs')
    self.assertNotEqual(id(obj2), int(out))
