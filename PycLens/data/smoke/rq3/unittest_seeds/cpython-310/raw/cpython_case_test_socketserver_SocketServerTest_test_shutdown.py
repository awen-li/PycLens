# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: SocketServerTest_test_shutdown

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MyServer(socketserver.TCPServer):
        pass

    class MyHandler(socketserver.StreamRequestHandler):
        pass
    threads = []
    for i in range(20):
        s = MyServer((HOST, 0), MyHandler)
        t = threading.Thread(name='MyServer serving', target=s.serve_forever, kwargs={'poll_interval': 0.01})
        t.daemon = True
        threads.append((t, s))
    for (t, s) in threads:
        t.start()
        s.shutdown()
    for (t, s) in threads:
        t.join()
        s.server_close()
