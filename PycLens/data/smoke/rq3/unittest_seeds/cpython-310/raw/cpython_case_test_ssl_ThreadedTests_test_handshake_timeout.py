# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_handshake_timeout

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = socket.socket(socket.AF_INET)
    host = '127.0.0.1'
    port = socket_helper.bind_port(server)
    started = threading.Event()
    finish = False

    def serve():
        server.listen()
        started.set()
        conns = []
        while not finish:
            (r, w, e) = select.select([server], [], [], 0.1)
            if server in r:
                conns.append(server.accept()[0])
        for sock in conns:
            sock.close()
    t = threading.Thread(target=serve)
    t.start()
    started.wait()
    try:
        try:
            c = socket.socket(socket.AF_INET)
            c.settimeout(0.2)
            c.connect((host, port))
            self.assertRaisesRegex(TimeoutError, 'timed out', test_wrap_socket, c)
        finally:
            c.close()
        try:
            c = socket.socket(socket.AF_INET)
            c = test_wrap_socket(c)
            c.settimeout(0.2)
            self.assertRaisesRegex(TimeoutError, 'timed out', c.connect, (host, port))
        finally:
            c.close()
    finally:
        finish = True
        t.join()
        server.close()
