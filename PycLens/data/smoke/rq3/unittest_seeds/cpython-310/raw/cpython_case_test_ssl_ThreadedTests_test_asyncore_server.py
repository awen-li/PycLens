# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_asyncore_server

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if support.verbose:
        sys.stdout.write('\n')
    indata = b'FOO\n'
    server = AsyncoreEchoServer(CERTFILE)
    with server:
        s = test_wrap_socket(socket.socket())
        s.connect(('127.0.0.1', server.port))
        if support.verbose:
            sys.stdout.write(' client:  sending %r...\n' % indata)
        s.write(indata)
        outdata = s.read()
        if support.verbose:
            sys.stdout.write(' client:  read %r\n' % outdata)
        if outdata != indata.lower():
            self.fail('bad data <<%r>> (%d) received; expected <<%r>> (%d)\n' % (outdata[:20], len(outdata), indata[:20].lower(), len(indata)))
        s.write(b'over\n')
        if support.verbose:
            sys.stdout.write(' client:  closing connection.\n')
        s.close()
        if support.verbose:
            sys.stdout.write(' client:  connection closed.\n')
