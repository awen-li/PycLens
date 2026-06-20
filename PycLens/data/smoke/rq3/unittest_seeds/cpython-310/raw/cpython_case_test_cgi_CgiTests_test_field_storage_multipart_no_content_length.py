# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_field_storage_multipart_no_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = BytesIO(b'--MyBoundary\nContent-Disposition: form-data; name="my-arg"; filename="foo"\n\nTest\n\n--MyBoundary--\n')
    env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart/form-data; boundary=MyBoundary', 'wsgi.input': fp}
    fields = cgi.FieldStorage(fp, environ=env)
    self.assertEqual(len(fields['my-arg'].file.read()), 5)
