# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_data

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertFalse(self.get.data)
    self.assertEqual('GET', self.get.get_method())
    self.get.data = 'spam'
    self.assertTrue(self.get.data)
    self.assertEqual('POST', self.get.get_method())
