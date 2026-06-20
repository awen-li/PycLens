# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_parse_multipart_without_content_length

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    POSTDATA = '--JfISa01\nContent-Disposition: form-data; name="submit-name"\n\njust a string\n\n--JfISa01--\n'
    fp = BytesIO(POSTDATA.encode('latin1'))
    env = {'boundary': 'JfISa01'.encode('latin1')}
    result = cgi.parse_multipart(fp, env)
    expected = {'submit-name': ['just a string\n']}
    self.assertEqual(result, expected)
