# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_part_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    BOUNDARY = 'JfISa01'
    POSTDATA = '--JfISa01\nContent-Disposition: form-data; name="submit-name"\nContent-Length: 5\n\nLarry\n--JfISa01'
    env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart/form-data; boundary={}'.format(BOUNDARY), 'CONTENT_LENGTH': str(len(POSTDATA))}
    fp = BytesIO(POSTDATA.encode('latin-1'))
    fs = cgi.FieldStorage(fp, environ=env, encoding='latin-1')
    self.assertEqual(len(fs.list), 1)
    self.assertEqual(fs.list[0].name, 'submit-name')
    self.assertEqual(fs.list[0].value, 'Larry')
