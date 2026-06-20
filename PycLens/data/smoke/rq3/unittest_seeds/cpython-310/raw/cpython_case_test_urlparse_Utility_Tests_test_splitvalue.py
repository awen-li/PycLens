# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urlparse.py
# case: Utility_Tests_test_splitvalue

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    splitvalue = urllib.parse._splitvalue
    self.assertEqual(splitvalue('foo=bar'), ('foo', 'bar'))
    self.assertEqual(splitvalue('foo='), ('foo', ''))
    self.assertEqual(splitvalue('=bar'), ('', 'bar'))
    self.assertEqual(splitvalue('foobar'), ('foobar', None))
    self.assertEqual(splitvalue('foo=bar=baz'), ('foo', 'bar=baz'))
