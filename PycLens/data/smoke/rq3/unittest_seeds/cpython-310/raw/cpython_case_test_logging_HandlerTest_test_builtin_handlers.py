# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_logging.py
# case: HandlerTest_test_builtin_handlers

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if sys.platform in ('linux', 'darwin'):
        for existing in (True, False):
            (fd, fn) = tempfile.mkstemp()
            os.close(fd)
            if not existing:
                os.unlink(fn)
            h = logging.handlers.WatchedFileHandler(fn, encoding='utf-8', delay=True)
            if existing:
                (dev, ino) = (h.dev, h.ino)
                self.assertEqual(dev, -1)
                self.assertEqual(ino, -1)
                r = logging.makeLogRecord({'msg': 'Test'})
                h.handle(r)
                os.unlink(fn)
                self.assertFalse(os.path.exists(fn))
                h.handle(r)
                self.assertTrue(os.path.exists(fn))
            else:
                self.assertEqual(h.dev, -1)
                self.assertEqual(h.ino, -1)
            h.close()
            if existing:
                os.unlink(fn)
        if sys.platform == 'darwin':
            sockname = '/var/run/syslog'
        else:
            sockname = '/dev/log'
        try:
            h = logging.handlers.SysLogHandler(sockname)
            self.assertEqual(h.facility, h.LOG_USER)
            self.assertTrue(h.unixsocket)
            h.close()
        except OSError:
            pass
    for method in ('GET', 'POST', 'PUT'):
        if method == 'PUT':
            self.assertRaises(ValueError, logging.handlers.HTTPHandler, 'localhost', '/log', method)
        else:
            h = logging.handlers.HTTPHandler('localhost', '/log', method)
            h.close()
    h = logging.handlers.BufferingHandler(0)
    r = logging.makeLogRecord({})
    self.assertTrue(h.shouldFlush(r))
    h.close()
    h = logging.handlers.BufferingHandler(1)
    self.assertFalse(h.shouldFlush(r))
    h.close()
