# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: SSLObjectTests_test_unwrap

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_ctx, server_ctx, hostname) = testing_context()
    c_in = ssl.MemoryBIO()
    c_out = ssl.MemoryBIO()
    s_in = ssl.MemoryBIO()
    s_out = ssl.MemoryBIO()
    client = client_ctx.wrap_bio(c_in, c_out, server_hostname=hostname)
    server = server_ctx.wrap_bio(s_in, s_out, server_side=True)
    for _ in range(5):
        try:
            client.do_handshake()
        except ssl.SSLWantReadError:
            pass
        if c_out.pending:
            s_in.write(c_out.read())
        try:
            server.do_handshake()
        except ssl.SSLWantReadError:
            pass
        if s_out.pending:
            c_in.write(s_out.read())
    client.do_handshake()
    server.do_handshake()
    with self.assertRaises(ssl.SSLWantReadError):
        client.unwrap()
    s_in.write(c_out.read())
    server.unwrap()
    c_in.write(s_out.read())
    client.unwrap()
