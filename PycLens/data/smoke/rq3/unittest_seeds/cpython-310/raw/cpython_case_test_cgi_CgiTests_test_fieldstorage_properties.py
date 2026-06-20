# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_properties

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fs = cgi.FieldStorage()
    self.assertFalse(fs)
    self.assertIn('FieldStorage', repr(fs))
    self.assertEqual(list(fs), list(fs.keys()))
    fs.list.append(namedtuple('MockFieldStorage', 'name')('fieldvalue'))
    self.assertTrue(fs)
