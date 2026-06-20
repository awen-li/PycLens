# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_asyncore.py
# case: DispatcherWithSendTests_test_send

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    evt = threading.Event()
    sock = socket.socket()
    sock.settimeout(3)
    port = socket_helper.bind_port(sock)
    cap = BytesIO()
    args = (evt, cap, sock)
    t = threading.Thread(target=capture_server, args=args)
    t.start()
    try:
        time.sleep(0.2)
        data = b"Suppose there isn't a 16-ton weight?"
        d = dispatcherwithsend_noread()
        d.create_socket()
        d.connect((socket_helper.HOST, port))
        time.sleep(0.1)
        d.send(data)
        d.send(data)
        d.send(b'\n')
        n = 1000
        while d.out_buffer and n > 0:
            asyncore.poll()
            n -= 1
        evt.wait()
        self.assertEqual(cap.getvalue(), data * 2)
    finally:
        threading_helper.join_thread(t)
