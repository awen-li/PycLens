# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: GzipServerTestCase_test_bad_gzip_request

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    t = self.Transport()
    t.encode_threshold = None
    t.fake_gzip = True
    p = xmlrpclib.ServerProxy(URL, transport=t)
    cm = self.assertRaisesRegex(xmlrpclib.ProtocolError, re.compile('\\b400\\b'))
    with cm:
        p.pow(6, 8)
    p('close')()
