# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asynchat.py
# case: TestAsynchat_test_close_when_done

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (s, event) = start_echo_server()
    s.start_resend_event = threading.Event()
    c = echo_client(b'\n', s.port)
    c.push(b"hello world\nI'm not dead yet!\n")
    c.push(SERVER_QUIT)
    c.close_when_done()
    asyncore.loop(use_poll=self.usepoll, count=300, timeout=0.01)
    s.start_resend_event.set()
    threading_helper.join_thread(s)
    self.assertEqual(c.contents, [])
    self.assertGreater(len(s.buffer), 0)
