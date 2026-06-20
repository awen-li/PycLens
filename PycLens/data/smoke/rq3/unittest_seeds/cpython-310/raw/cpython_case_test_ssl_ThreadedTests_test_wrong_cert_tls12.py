# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_wrong_cert_tls12

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    (client_context, server_context, hostname) = testing_context()
    client_context.load_cert_chain(CERTFILE)
    server_context.verify_mode = ssl.CERT_REQUIRED
    client_context.maximum_version = ssl.TLSVersion.TLSv1_2
    server = ThreadedEchoServer(context=server_context, chatty=True, connectionchatty=True)
    with server, client_context.wrap_socket(socket.socket(), server_hostname=hostname) as s:
        try:
            s.connect((HOST, server.port))
        except ssl.SSLError as e:
            if support.verbose:
                sys.stdout.write('\nSSLError is %r\n' % e)
        except OSError as e:
            if e.errno != errno.ECONNRESET:
                raise
            if support.verbose:
                sys.stdout.write('\nsocket.error is %r\n' % e)
        else:
            self.fail('Use of invalid cert should have failed!')
