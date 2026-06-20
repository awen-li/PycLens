# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib2.py
# case: MiscTests_test_HTTPError_interface

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    msg = 'something bad happened'
    url = code = fp = None
    hdrs = 'Content-Length: 42'
    err = urllib.error.HTTPError(url, code, msg, hdrs, fp)
    self.assertTrue(hasattr(err, 'reason'))
    self.assertEqual(err.reason, 'something bad happened')
    self.assertTrue(hasattr(err, 'headers'))
    self.assertEqual(err.headers, 'Content-Length: 42')
    expected_errmsg = 'HTTP Error %s: %s' % (err.code, err.msg)
    self.assertEqual(str(err), expected_errmsg)
    expected_errmsg = '<HTTPError %s: %r>' % (err.code, err.msg)
    self.assertEqual(repr(err), expected_errmsg)
