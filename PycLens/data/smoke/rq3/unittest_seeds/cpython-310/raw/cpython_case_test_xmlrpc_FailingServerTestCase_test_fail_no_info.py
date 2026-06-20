# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: FailingServerTestCase_test_fail_no_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xmlrpc.server.SimpleXMLRPCRequestHandler.MessageClass = FailingMessageClass
    try:
        p = xmlrpclib.ServerProxy(URL)
        p.pow(6, 8)
    except (xmlrpclib.ProtocolError, OSError) as e:
        if not is_unavailable_exception(e) and hasattr(e, 'headers'):
            self.assertTrue(e.headers.get('X-exception') is None)
            self.assertTrue(e.headers.get('X-traceback') is None)
    else:
        self.fail('ProtocolError not raised')
