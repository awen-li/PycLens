# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestHdrsTests_test_request_headers_methods

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = 'http://example.com'
    req = Request(url, headers={'Spam-eggs': 'blah'})
    self.assertTrue(req.has_header('Spam-eggs'))
    self.assertEqual(req.header_items(), [('Spam-eggs', 'blah')])
    req.add_header('Foo-Bar', 'baz')
    self.assertEqual(sorted(req.header_items()), [('Foo-bar', 'baz'), ('Spam-eggs', 'blah')])
    self.assertFalse(req.has_header('Not-there'))
    self.assertIsNone(req.get_header('Not-there'))
    self.assertEqual(req.get_header('Not-there', 'default'), 'default')
    req.remove_header('Spam-eggs')
    self.assertFalse(req.has_header('Spam-eggs'))
    req.add_unredirected_header('Unredirected-spam', 'Eggs')
    self.assertTrue(req.has_header('Unredirected-spam'))
    req.remove_header('Unredirected-spam')
    self.assertFalse(req.has_header('Unredirected-spam'))
