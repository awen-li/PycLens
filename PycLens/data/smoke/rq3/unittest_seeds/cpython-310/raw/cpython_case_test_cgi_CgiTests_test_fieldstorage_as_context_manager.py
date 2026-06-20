# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_as_context_manager

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = BytesIO(b'x' * 10)
    env = {'REQUEST_METHOD': 'PUT'}
    with cgi.FieldStorage(fp=fp, environ=env) as fs:
        content = fs.file.read()
        self.assertFalse(fs.file.closed)
    self.assertTrue(fs.file.closed)
    self.assertEqual(content, 'x' * 10)
    with self.assertRaisesRegex(ValueError, 'I/O operation on closed file'):
        fs.file.read()
