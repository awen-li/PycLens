# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual('POST', self.post.get_method())
    self.assertEqual('GET', self.get.get_method())
    self.assertEqual('HEAD', self.head.get_method())
    self.assertEqual('PUT', self.put.get_method())
    self.assertEqual('POST', self.force_post.get_method())
