# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_wsgiref.py
# case: IntegrationTests_test_interrupted_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pthread_kill = support.get_attribute(signal, 'pthread_kill')

    def app(environ, start_response):
        start_response('200 OK', [])
        return [b'\x00' * support.SOCK_MAX_SIZE]

    class WsgiHandler(NoLogRequestHandler, WSGIRequestHandler):
        pass
    server = make_server(socket_helper.HOST, 0, app, handler_class=WsgiHandler)
    self.addCleanup(server.server_close)
    interrupted = threading.Event()

    def signal_handler(signum, frame):
        interrupted.set()
    original = signal.signal(signal.SIGUSR1, signal_handler)
    self.addCleanup(signal.signal, signal.SIGUSR1, original)
    received = None
    main_thread = threading.get_ident()

    def run_client():
        http = HTTPConnection(*server.server_address)
        http.request('GET', '/')
        with http.getresponse() as response:
            response.read(100)
            while True:
                pthread_kill(main_thread, signal.SIGUSR1)
                if interrupted.wait(timeout=float(1)):
                    break
            nonlocal received
            received = len(response.read())
        http.close()
    background = threading.Thread(target=run_client)
    background.start()
    server.handle_request()
    background.join()
    self.assertEqual(received, support.SOCK_MAX_SIZE - 100)
