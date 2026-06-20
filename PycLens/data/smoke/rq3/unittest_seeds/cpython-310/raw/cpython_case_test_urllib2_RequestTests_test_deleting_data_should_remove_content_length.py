# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestTests_test_deleting_data_should_remove_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertNotIn('Content-length', self.get.unredirected_hdrs)
    self.get.data = 'foo'
    self.get.add_unredirected_header('Content-length', 3)
    self.assertEqual(3, self.get.unredirected_hdrs['Content-length'])
    del self.get.data
    self.assertNotIn('Content-length', self.get.unredirected_hdrs)
