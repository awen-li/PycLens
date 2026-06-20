# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_server_accept

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_ctx, server_ctx, hostname) = testing_context()
    server = socket.socket(socket.AF_INET)
    host = '127.0.0.1'
    port = socket_helper.bind_port(server)
    server = server_ctx.wrap_socket(server, server_side=True)
    self.assertTrue(server.server_side)
    evt = threading.Event()
    remote = None
    peer = None

    def serve():
        nonlocal remote, peer
        server.listen()
        evt.set()
        (remote, peer) = server.accept()
        remote.send(remote.recv(4))
    t = threading.Thread(target=serve)
    t.start()
    evt.wait()
    client = client_ctx.wrap_socket(socket.socket(), server_hostname=hostname)
    client.connect((hostname, port))
    client.send(b'data')
    client.recv()
    client_addr = client.getsockname()
    client.close()
    t.join()
    remote.close()
    server.close()
    self.assertIsInstance(remote, ssl.SSLSocket)
    self.assertEqual(peer, client_addr)
