# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_multipart_w3c

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart/form-data; boundary={}'.format(BOUNDARY_W3), 'CONTENT_LENGTH': str(len(POSTDATA_W3))}
    fp = BytesIO(POSTDATA_W3.encode('latin-1'))
    fs = cgi.FieldStorage(fp, environ=env, encoding='latin-1')
    self.assertEqual(len(fs.list), 2)
    self.assertEqual(fs.list[0].name, 'submit-name')
    self.assertEqual(fs.list[0].value, 'Larry')
    self.assertEqual(fs.list[1].name, 'files')
    files = fs.list[1].value
    self.assertEqual(len(files), 2)
    expect = [{'name': None, 'filename': 'file1.txt', 'value': b'... contents of file1.txt ...'}, {'name': None, 'filename': 'file2.gif', 'value': b'...contents of file2.gif...'}]
    for x in range(len(files)):
        for (k, exp) in expect[x].items():
            got = getattr(files[x], k)
            self.assertEqual(got, exp)
