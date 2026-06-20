# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_cgi.py
# case: CgiTests_test_parse_multipart

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fp = BytesIO(POSTDATA.encode('latin1'))
    env = {'boundary': BOUNDARY.encode('latin1'), 'CONTENT-LENGTH': '558'}
    result = cgi.parse_multipart(fp, env)
    expected = {'submit': [' Add '], 'id': ['1234'], 'file': [b'Testing 123.\n'], 'title': ['']}
    self.assertEqual(result, expected)
