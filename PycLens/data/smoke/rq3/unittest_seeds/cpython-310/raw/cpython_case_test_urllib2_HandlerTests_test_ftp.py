# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_ftp

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class MockFTPWrapper:

        def __init__(self, data):
            self.data = data

        def retrfile(self, filename, filetype):
            (self.filename, self.filetype) = (filename, filetype)
            return (io.StringIO(self.data), len(self.data))

        def close(self):
            pass

    class NullFTPHandler(urllib.request.FTPHandler):

        def __init__(self, data):
            self.data = data

        def connect_ftp(self, user, passwd, host, port, dirs, timeout=socket._GLOBAL_DEFAULT_TIMEOUT):
            (self.user, self.passwd) = (user, passwd)
            (self.host, self.port) = (host, port)
            self.dirs = dirs
            self.ftpwrapper = MockFTPWrapper(self.data)
            return self.ftpwrapper
    import ftplib
    data = 'rheum rhaponicum'
    h = NullFTPHandler(data)
    h.parent = MockOpener()
    for (url, host, port, user, passwd, type_, dirs, filename, mimetype) in [('ftp://localhost/foo/bar/baz.html', 'localhost', ftplib.FTP_PORT, '', '', 'I', ['foo', 'bar'], 'baz.html', 'text/html'), ('ftp://parrot@localhost/foo/bar/baz.html', 'localhost', ftplib.FTP_PORT, 'parrot', '', 'I', ['foo', 'bar'], 'baz.html', 'text/html'), ('ftp://%25parrot@localhost/foo/bar/baz.html', 'localhost', ftplib.FTP_PORT, '%parrot', '', 'I', ['foo', 'bar'], 'baz.html', 'text/html'), ('ftp://%2542parrot@localhost/foo/bar/baz.html', 'localhost', ftplib.FTP_PORT, '%42parrot', '', 'I', ['foo', 'bar'], 'baz.html', 'text/html'), ('ftp://localhost:80/foo/bar/', 'localhost', 80, '', '', 'D', ['foo', 'bar'], '', None), ('ftp://localhost/baz.gif;type=a', 'localhost', ftplib.FTP_PORT, '', '', 'A', [], 'baz.gif', None)]:
        req = Request(url)
        req.timeout = None
        r = h.ftp_open(req)
        self.assertEqual(h.user, user)
        self.assertEqual(h.passwd, passwd)
        self.assertEqual(h.host, socket.gethostbyname(host))
        self.assertEqual(h.port, port)
        self.assertEqual(h.dirs, dirs)
        self.assertEqual(h.ftpwrapper.filename, filename)
        self.assertEqual(h.ftpwrapper.filetype, type_)
        headers = r.info()
        self.assertEqual(headers.get('Content-type'), mimetype)
        self.assertEqual(int(headers['Content-length']), len(data))
