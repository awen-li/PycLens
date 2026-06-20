# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_doubleslash

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    h = urllib.request.AbstractHTTPHandler()
    h.parent = MockOpener()
    data = b''
    ds_urls = ['http://example.com/foo/bar/baz.html', 'http://example.com//foo/bar/baz.html', 'http://example.com/foo//bar/baz.html', 'http://example.com/foo/bar//baz.html']
    for ds_url in ds_urls:
        ds_req = Request(ds_url, data)
        np_ds_req = h.do_request_(ds_req)
        self.assertEqual(np_ds_req.unredirected_hdrs['Host'], 'example.com')
        ds_req.set_proxy('someproxy:3128', None)
        p_ds_req = h.do_request_(ds_req)
        self.assertEqual(p_ds_req.unredirected_hdrs['Host'], 'example.com')
