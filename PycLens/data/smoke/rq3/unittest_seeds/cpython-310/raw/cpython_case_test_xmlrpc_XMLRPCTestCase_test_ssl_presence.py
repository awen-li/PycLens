# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: XMLRPCTestCase_test_ssl_presence

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        import ssl
    except ImportError:
        has_ssl = False
    else:
        has_ssl = True
    try:
        xmlrpc.client.ServerProxy('https://localhost:9999').bad_function()
    except NotImplementedError:
        self.assertFalse(has_ssl, "xmlrpc client's error with SSL support")
    except OSError:
        self.assertTrue(has_ssl)
