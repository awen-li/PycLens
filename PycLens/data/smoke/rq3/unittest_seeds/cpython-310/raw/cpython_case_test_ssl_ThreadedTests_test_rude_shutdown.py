# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_rude_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    listener_ready = threading.Event()
    listener_gone = threading.Event()
    s = socket.socket()
    port = socket_helper.bind_port(s, HOST)

    def listener():
        s.listen()
        listener_ready.set()
        (newsock, addr) = s.accept()
        newsock.close()
        s.close()
        listener_gone.set()

    def connector():
        listener_ready.wait()
        with socket.socket() as c:
            c.connect((HOST, port))
            listener_gone.wait()
            try:
                ssl_sock = test_wrap_socket(c)
            except OSError:
                pass
            else:
                self.fail('connecting to closed SSL socket should have failed')
    t = threading.Thread(target=listener)
    t.start()
    try:
        connector()
    finally:
        t.join()
