# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_interpreters.py
# case: TestSendRecv_test_send_recv_different_threads

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (r, s) = interpreters.create_channel()

    def f():
        while True:
            try:
                obj = r.recv()
                break
            except interpreters.ChannelEmptyError:
                time.sleep(0.1)
        s.send(obj)
    t = threading.Thread(target=f)
    t.start()
    orig = b'spam'
    s.send(orig)
    t.join()
    obj = r.recv()
    self.assertEqual(obj, orig)
    self.assertIsNot(obj, orig)
