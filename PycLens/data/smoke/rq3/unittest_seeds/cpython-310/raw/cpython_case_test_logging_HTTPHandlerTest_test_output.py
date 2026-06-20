# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: HTTPHandlerTest_test_output

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    logger = logging.getLogger('http')
    root_logger = self.root_logger
    root_logger.removeHandler(self.root_logger.handlers[0])
    for secure in (False, True):
        addr = ('localhost', 0)
        if secure:
            try:
                import ssl
            except ImportError:
                sslctx = None
            else:
                here = os.path.dirname(__file__)
                localhost_cert = os.path.join(here, 'keycert.pem')
                sslctx = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
                sslctx.load_cert_chain(localhost_cert)
                context = ssl.create_default_context(cafile=localhost_cert)
        else:
            sslctx = None
            context = None
        self.server = server = TestHTTPServer(addr, self.handle_request, 0.01, sslctx=sslctx)
        server.start()
        server.ready.wait()
        host = 'localhost:%d' % server.server_port
        secure_client = secure and sslctx
        self.h_hdlr = logging.handlers.HTTPHandler(host, '/frob', secure=secure_client, context=context, credentials=('foo', 'bar'))
        self.log_data = None
        root_logger.addHandler(self.h_hdlr)
        for method in ('GET', 'POST'):
            self.h_hdlr.method = method
            self.handled.clear()
            msg = 'späm'
            logger.error(msg)
            self.handled.wait()
            self.assertEqual(self.log_data.path, '/frob')
            self.assertEqual(self.command, method)
            if method == 'GET':
                d = parse_qs(self.log_data.query)
            else:
                d = parse_qs(self.post_data.decode('utf-8'))
            self.assertEqual(d['name'], ['http'])
            self.assertEqual(d['funcName'], ['test_output'])
            self.assertEqual(d['msg'], [msg])
        self.server.stop()
        self.root_logger.removeHandler(self.h_hdlr)
        self.h_hdlr.close()
