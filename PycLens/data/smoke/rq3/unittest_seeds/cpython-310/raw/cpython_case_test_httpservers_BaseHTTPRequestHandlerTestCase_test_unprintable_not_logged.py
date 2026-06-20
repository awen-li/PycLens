# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: BaseHTTPRequestHandlerTestCase_test_unprintable_not_logged

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.handler.client_address = ('127.0.0.1', 1337)
    log_message = BaseHTTPRequestHandler.log_message
    with mock.patch.object(sys, 'stderr', StringIO()) as fake_stderr:
        log_message(self.handler, '/foo')
        log_message(self.handler, '/\x1bbar\x00\x1b')
        log_message(self.handler, '/spam %s.', 'a')
        log_message(self.handler, '/spam %s.', '\x1b\x7f\x9f\xa0beans')
        log_message(self.handler, '"GET /foo\\b"ar\x07 HTTP/1.0"')
    stderr = fake_stderr.getvalue()
    self.assertNotIn('\x1b', stderr)
    self.assertNotIn('\x00', stderr)
    lines = stderr.splitlines()
    self.assertIn('/foo', lines[0])
    self.assertIn('/\\x1bbar\\x00\\x1b', lines[1])
    self.assertIn('/spam a.', lines[2])
    self.assertIn('/spam \\x1b\\x7f\\x9f\xa0beans.', lines[3])
    self.assertIn('"GET /foo\\\\b"ar\\x07 HTTP/1.0"', lines[4])
