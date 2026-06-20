# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: HandlerTests_test_http_handler_debuglevel

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    o = OpenerDirector()
    h = MockHTTPSHandler(debuglevel=1)
    o.add_handler(h)
    o.open('https://www.example.com')
    self.assertEqual(h._debuglevel, 1)
