# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_networked_trusted_by_default_cert

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    support.requires('network')
    with socket_helper.transient_internet('www.python.org'):
        h = client.HTTPSConnection('www.python.org', 443)
        h.request('GET', '/')
        resp = h.getresponse()
        content_type = resp.getheader('content-type')
        resp.close()
        h.close()
        self.assertIn('text/html', content_type)
