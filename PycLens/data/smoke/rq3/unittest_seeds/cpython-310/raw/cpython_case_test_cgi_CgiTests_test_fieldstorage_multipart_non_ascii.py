# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_multipart_non_ascii

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    env = {'REQUEST_METHOD': 'POST', 'CONTENT_TYPE': 'multipart/form-data; boundary={}'.format(BOUNDARY), 'CONTENT_LENGTH': '558'}
    for encoding in ['iso-8859-1', 'utf-8']:
        fp = BytesIO(POSTDATA_NON_ASCII.encode(encoding))
        fs = cgi.FieldStorage(fp, environ=env, encoding=encoding)
        self.assertEqual(len(fs.list), 1)
        expect = [{'name': 'id', 'filename': None, 'value': 'çñ\x80'}]
        for x in range(len(fs.list)):
            for (k, exp) in expect[x].items():
                got = getattr(fs.list[x], k)
                self.assertEqual(got, exp)
