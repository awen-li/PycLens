# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: FailingServerTestCase_test_fail_with_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    xmlrpc.server.SimpleXMLRPCRequestHandler.MessageClass = FailingMessageClass
    xmlrpc.server.SimpleXMLRPCServer._send_traceback_header = True
    try:
        p = xmlrpclib.ServerProxy(URL)
        p.pow(6, 8)
    except (xmlrpclib.ProtocolError, OSError) as e:
        if not is_unavailable_exception(e) and hasattr(e, 'headers'):
            expected_err = "invalid literal for int() with base 10: 'I am broken'"
            self.assertEqual(e.headers.get('X-exception'), expected_err)
            self.assertTrue(e.headers.get('X-traceback') is not None)
    else:
        self.fail('ProtocolError not raised')
