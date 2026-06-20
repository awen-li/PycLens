# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_file

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import email.utils
    h = urllib.request.FileHandler()
    o = h.parent = MockOpener()
    TESTFN = os_helper.TESTFN
    urlpath = sanepathname2url(os.path.abspath(TESTFN))
    towrite = b'hello, world\n'
    urls = ['file://localhost%s' % urlpath, 'file://%s' % urlpath, 'file://%s%s' % (socket.gethostbyname('localhost'), urlpath)]
    try:
        localaddr = socket.gethostbyname(socket.gethostname())
    except socket.gaierror:
        localaddr = ''
    if localaddr:
        urls.append('file://%s%s' % (localaddr, urlpath))
    for url in urls:
        f = open(TESTFN, 'wb')
        try:
            try:
                f.write(towrite)
            finally:
                f.close()
            r = h.file_open(Request(url))
            try:
                data = r.read()
                headers = r.info()
                respurl = r.geturl()
            finally:
                r.close()
            stats = os.stat(TESTFN)
            modified = email.utils.formatdate(stats.st_mtime, usegmt=True)
        finally:
            os.remove(TESTFN)
        self.assertEqual(data, towrite)
        self.assertEqual(headers['Content-type'], 'text/plain')
        self.assertEqual(headers['Content-length'], '13')
        self.assertEqual(headers['Last-modified'], modified)
        self.assertEqual(respurl, url)
    for url in ['file://localhost:80%s' % urlpath, 'file:///file_does_not_exist.txt', 'file://not-a-local-host.com//dir/file.txt', 'file://%s:80%s/%s' % (socket.gethostbyname('localhost'), os.getcwd(), TESTFN), 'file://somerandomhost.ontheinternet.com%s/%s' % (os.getcwd(), TESTFN)]:
        try:
            f = open(TESTFN, 'wb')
            try:
                f.write(towrite)
            finally:
                f.close()
            self.assertRaises(urllib.error.URLError, h.file_open, Request(url))
        finally:
            os.remove(TESTFN)
    h = urllib.request.FileHandler()
    o = h.parent = MockOpener()
    for (url, ftp) in [('file://ftp.example.com//foo.txt', False), ('file://ftp.example.com///foo.txt', False), ('file://ftp.example.com/foo.txt', False), ('file://somehost//foo/something.txt', False), ('file://localhost//foo/something.txt', False)]:
        req = Request(url)
        try:
            h.file_open(req)
        except urllib.error.URLError:
            self.assertFalse(ftp)
        else:
            self.assertIs(o.req, req)
            self.assertEqual(req.type, 'ftp')
        self.assertEqual(req.type == 'ftp', ftp)
