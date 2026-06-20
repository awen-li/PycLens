# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_selector

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('/~jeremy/', self.get.selector)
    req = Request('http://www.python.org/')
    self.assertEqual('/', req.selector)
