# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_partial_post

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    with contextlib.closing(socket.create_connection((ADDR, PORT))) as conn:
        conn.send(f'POST /RPC2 HTTP/1.0\r\nContent-Length: 100\r\n\r\nbye HTTP/1.1\r\nHost: {ADDR}:{PORT}\r\nAccept-Encoding: identity\r\nContent-Length: 0\r\n\r\n'.encode('ascii'))
