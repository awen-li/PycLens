# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_socketserver.py
# case: SocketWriterTest_test_write

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    pthread_kill = test.support.get_attribute(signal, 'pthread_kill')

    class Handler(socketserver.StreamRequestHandler):

        def handle(self):
            self.server.sent1 = self.wfile.write(b'write data\n')
            self.server.received = self.rfile.readline()
            big_chunk = b'\x00' * test.support.SOCK_MAX_SIZE
            self.server.sent2 = self.wfile.write(big_chunk)
    server = socketserver.TCPServer((HOST, 0), Handler)
    self.addCleanup(server.server_close)
    interrupted = threading.Event()

    def signal_handler(signum, frame):
        interrupted.set()
    original = signal.signal(signal.SIGUSR1, signal_handler)
    self.addCleanup(signal.signal, signal.SIGUSR1, original)
    response1 = None
    received2 = None
    main_thread = threading.get_ident()

    def run_client():
        s = socket.socket(server.address_family, socket.SOCK_STREAM, socket.IPPROTO_TCP)
        with s, s.makefile('rb') as reader:
            s.connect(server.server_address)
            nonlocal response1
            response1 = reader.readline()
            s.sendall(b'client response\n')
            reader.read(100)
            while True:
                pthread_kill(main_thread, signal.SIGUSR1)
                if interrupted.wait(timeout=float(1)):
                    break
            nonlocal received2
            received2 = len(reader.read())
    background = threading.Thread(target=run_client)
    background.start()
    server.handle_request()
    background.join()
    self.assertEqual(server.sent1, len(response1))
    self.assertEqual(response1, b'write data\n')
    self.assertEqual(server.received, b'client response\n')
    self.assertEqual(server.sent2, test.support.SOCK_MAX_SIZE)
    self.assertEqual(received2, test.support.SOCK_MAX_SIZE - 100)
