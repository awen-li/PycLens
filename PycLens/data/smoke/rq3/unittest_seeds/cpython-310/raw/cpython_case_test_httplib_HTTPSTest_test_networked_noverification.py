# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httplib.py
# case: HTTPSTest_test_networked_noverification

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import ssl
    support.requires('network')
    with socket_helper.transient_internet('self-signed.pythontest.net'):
        context = ssl._create_unverified_context()
        h = client.HTTPSConnection('self-signed.pythontest.net', 443, context=context)
        h.request('GET', '/')
        resp = h.getresponse()
        h.close()
        self.assertIn('nginx', resp.getheader('server'))
        resp.close()
