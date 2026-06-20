# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_max_num_fields

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    data = '&'.join(['a=a'] * 11)
    environ = {'CONTENT_LENGTH': str(len(data)), 'CONTENT_TYPE': 'application/x-www-form-urlencoded', 'REQUEST_METHOD': 'POST'}
    with self.assertRaises(ValueError):
        cgi.FieldStorage(fp=BytesIO(data.encode()), environ=environ, max_num_fields=10)
    data = '---123\nContent-Disposition: form-data; name="a"\n\n3\n---123\nContent-Type: application/x-www-form-urlencoded\n\na=4\n---123\nContent-Type: application/x-www-form-urlencoded\n\na=5\n---123--\n'
    environ = {'CONTENT_LENGTH': str(len(data)), 'CONTENT_TYPE': 'multipart/form-data; boundary=-123', 'QUERY_STRING': 'a=1&a=2', 'REQUEST_METHOD': 'POST'}
    with self.assertRaises(ValueError):
        cgi.FieldStorage(fp=BytesIO(data.encode()), environ=environ, max_num_fields=4)
    cgi.FieldStorage(fp=BytesIO(data.encode()), environ=environ, max_num_fields=5)
