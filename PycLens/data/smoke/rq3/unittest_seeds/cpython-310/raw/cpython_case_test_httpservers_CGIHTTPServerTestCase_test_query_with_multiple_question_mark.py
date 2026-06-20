# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_httpservers.py
# case: CGIHTTPServerTestCase_test_query_with_multiple_question_mark

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    res = self.request('/cgi-bin/file4.py?a=b?c=d')
    self.assertEqual((b'a=b?c=d' + self.linesep, 'text/html', HTTPStatus.OK), (res.read(), res.getheader('Content-type'), res.status))
