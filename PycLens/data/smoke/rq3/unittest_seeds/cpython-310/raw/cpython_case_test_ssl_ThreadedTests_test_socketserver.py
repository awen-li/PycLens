# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ssl.py
# case: ThreadedTests_test_socketserver

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    server = make_https_server(self, certfile=SIGNED_CERTFILE)
    if support.verbose:
        sys.stdout.write('\n')
    with open(CERTFILE, 'rb') as f:
        d1 = f.read()
    d2 = ''
    url = 'https://localhost:%d/%s' % (server.port, os.path.split(CERTFILE)[1])
    context = ssl.create_default_context(cafile=SIGNING_CA)
    f = urllib.request.urlopen(url, context=context)
    try:
        dlen = f.info().get('content-length')
        if dlen and int(dlen) > 0:
            d2 = f.read(int(dlen))
            if support.verbose:
                sys.stdout.write(" client: read %d bytes from remote server '%s'\n" % (len(d2), server))
    finally:
        f.close()
    self.assertEqual(d1, d2)
