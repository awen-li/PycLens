# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: RequestTests_test_with_method_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    Request = urllib.request.Request
    request = Request('http://www.python.org', method='HEAD')
    self.assertEqual(request.method, 'HEAD')
    self.assertEqual(request.get_method(), 'HEAD')
    request = Request('http://www.python.org', {}, method='HEAD')
    self.assertEqual(request.method, 'HEAD')
    self.assertEqual(request.get_method(), 'HEAD')
    request = Request('http://www.python.org', method='GET')
    self.assertEqual(request.get_method(), 'GET')
    request.method = 'HEAD'
    self.assertEqual(request.get_method(), 'HEAD')
