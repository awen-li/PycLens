# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: BasicTest_test_response_fileno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    serv = socket.create_server((HOST, 0))
    self.addCleanup(serv.close)
    result = None

    def run_server():
        [conn, address] = serv.accept()
        with conn, conn.makefile('rb') as reader:
            while True:
                line = reader.readline()
                if not line.rstrip(b'\r\n'):
                    break
            conn.sendall(b'HTTP/1.1 200 Connection established\r\n\r\n')
            nonlocal result
            result = reader.read()
    thread = threading.Thread(target=run_server)
    thread.start()
    self.addCleanup(thread.join, float(1))
    conn = client.HTTPConnection(*serv.getsockname())
    conn.request('CONNECT', 'dummy:1234')
    response = conn.getresponse()
    try:
        self.assertEqual(response.status, client.OK)
        s = socket.socket(fileno=response.fileno())
        try:
            s.sendall(b'proxied data\n')
        finally:
            s.detach()
    finally:
        response.close()
        conn.close()
    thread.join()
    self.assertEqual(result, b'proxied data\n')
