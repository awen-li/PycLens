# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: SMTPHandlerTest_test_basic

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    sockmap = {}
    server = TestSMTPServer((socket_helper.HOST, 0), self.process_message, 0.001, sockmap)
    server.start()
    addr = (socket_helper.HOST, server.port)
    h = logging.handlers.SMTPHandler(addr, 'me', 'you', 'Log', timeout=self.TIMEOUT)
    self.assertEqual(h.toaddrs, ['you'])
    self.messages = []
    r = logging.makeLogRecord({'msg': 'Hello ✓'})
    self.handled = threading.Event()
    h.handle(r)
    self.handled.wait(self.TIMEOUT)
    server.stop()
    self.assertTrue(self.handled.is_set())
    self.assertEqual(len(self.messages), 1)
    (peer, mailfrom, rcpttos, data) = self.messages[0]
    self.assertEqual(mailfrom, 'me')
    self.assertEqual(rcpttos, ['you'])
    self.assertIn('\nSubject: Log\n', data)
    self.assertTrue(data.endswith('\n\nHello ✓'))
    h.close()
