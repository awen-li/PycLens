# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_nonascii_methodname

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    try:
        p = xmlrpclib.ServerProxy(URL, encoding='ascii')
        self.assertEqual(p.têšt(42), 42)
    except (xmlrpclib.ProtocolError, socket.error) as e:
        if not is_unavailable_exception(e):
            self.fail('%s\n%s' % (e, getattr(e, 'headers', '')))
