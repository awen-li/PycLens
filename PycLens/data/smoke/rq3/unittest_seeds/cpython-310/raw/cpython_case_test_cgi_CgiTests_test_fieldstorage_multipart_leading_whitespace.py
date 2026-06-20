# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_multipart_leading_whitespace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart/form-data; boundary={}'.format(BOUNDARY), 'CONTENT_LENGTH': '560'}
    fp = BytesIO(b'\r\n' + POSTDATA.encode('latin-1'))
    fs = cgi.FieldStorage(fp, environ=env, encoding='latin-1')
    self.assertEqual(len(fs.list), 4)
    expect = [{'name': 'id', 'filename': None, 'value': '1234'}, {'name': 'title', 'filename': None, 'value': ''}, {'name': 'file', 'filename': 'test.txt', 'value': b'Testing 123.\n'}, {'name': 'submit', 'filename': None, 'value': ' Add '}]
    for x in range(len(fs.list)):
        for (k, exp) in expect[x].items():
            got = getattr(fs.list[x], k)
            self.assertEqual(got, exp)
