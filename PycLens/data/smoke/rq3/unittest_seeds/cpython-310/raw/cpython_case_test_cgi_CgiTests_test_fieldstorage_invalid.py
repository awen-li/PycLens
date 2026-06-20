# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_invalid

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertRaises(TypeError, cgi.FieldStorage, 'not-a-file-obj', environ={'REQUEST_METHOD': 'PUT'})
    self.assertRaises(TypeError, cgi.FieldStorage, 'foo', 'bar')
    fs = cgi.FieldStorage(headers={'content-type': 'text/plain'})
    self.assertRaises(TypeError, bool, fs)
