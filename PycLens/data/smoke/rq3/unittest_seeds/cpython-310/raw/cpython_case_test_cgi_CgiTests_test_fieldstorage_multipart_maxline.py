# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_fieldstorage_multipart_maxline

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    maxline = 1 << 16
    self.maxDiff = None

    def check(content):
        data = '---123\nContent-Disposition: form-data; name="upload"; filename="fake.txt"\nContent-Type: text/plain\n\n%s\n---123--\n'.replace('\n', '\r\n') % content
        environ = {'CONTENT_LENGTH': str(len(data)), 'CONTENT_TYPE': 'multipart/form-data; boundary=-123', 'REQUEST_METHOD': 'POST'}
        self.assertEqual(gen_result(data, environ), {'upload': content.encode('latin1')})
    check('x' * (maxline - 1))
    check('x' * (maxline - 1) + '\r')
    check('x' * (maxline - 1) + '\r' + 'y' * (maxline - 1))
