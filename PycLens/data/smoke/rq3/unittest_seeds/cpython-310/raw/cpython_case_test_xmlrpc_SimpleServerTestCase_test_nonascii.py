# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_xmlrpc.py
# case: SimpleServerTestCase_test_nonascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    start_string = 'Pŷt'
    end_string = 'hơn'
    try:
        p = xmlrpclib.ServerProxy(URL)
        self.assertEqual(p.add(start_string, end_string), start_string + end_string)
    except (xmlrpclib.ProtocolError, OSError) as e:
        if not is_unavailable_exception(e):
            self.fail('%s\n%s' % (e, getattr(e, 'headers', '')))
