# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: RequestHdrsTests_test_request_headers_dict

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    url = 'http://example.com'
    self.assertEqual(Request(url, headers={'Spam-eggs': 'blah'}).headers['Spam-eggs'], 'blah')
    self.assertEqual(Request(url, headers={'spam-EggS': 'blah'}).headers['Spam-eggs'], 'blah')
