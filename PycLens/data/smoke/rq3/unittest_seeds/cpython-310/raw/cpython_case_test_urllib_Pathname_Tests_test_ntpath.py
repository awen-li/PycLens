# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: Pathname_Tests_test_ntpath

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = ('/C:/', '///C:/', '/C|//')
    expect = 'C:\\'
    for url in given:
        result = urllib.request.url2pathname(url)
        self.assertEqual(expect, result, 'urllib.request..url2pathname() failed; %s != %s' % (expect, result))
    given = '///C|/path'
    expect = 'C:\\path'
    result = urllib.request.url2pathname(given)
    self.assertEqual(expect, result, 'urllib.request.url2pathname() failed; %s != %s' % (expect, result))
