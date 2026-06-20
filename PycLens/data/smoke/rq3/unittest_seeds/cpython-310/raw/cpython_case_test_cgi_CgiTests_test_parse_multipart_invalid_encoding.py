# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_parse_multipart_invalid_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    BOUNDARY = 'JfISa01'
    POSTDATA = '--JfISa01\nContent-Disposition: form-data; name="submit-name"\nContent-Length: 3\n\n☃\n--JfISa01'
    fp = BytesIO(POSTDATA.encode('utf8'))
    env = {'boundary': BOUNDARY.encode('latin1'), 'CONTENT-LENGTH': str(len(POSTDATA.encode('utf8')))}
    result = cgi.parse_multipart(fp, env, encoding='ascii', errors='surrogateescape')
    expected = {'submit-name': ['\udce2\udc98\udc83']}
    self.assertEqual(result, expected)
    self.assertEqual('☃'.encode('utf8'), result['submit-name'][0].encode('utf8', 'surrogateescape'))
