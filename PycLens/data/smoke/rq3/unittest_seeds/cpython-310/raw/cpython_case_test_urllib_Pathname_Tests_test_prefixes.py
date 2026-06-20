# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: Pathname_Tests_test_prefixes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = '\\\\?\\C:\\dir'
    expect = '///C:/dir'
    result = urllib.request.pathname2url(given)
    self.assertEqual(expect, result, 'pathname2url() failed; %s != %s' % (expect, result))
    given = '\\\\?\\unc\\server\\share\\dir'
    expect = '/server/share/dir'
    result = urllib.request.pathname2url(given)
    self.assertEqual(expect, result, 'pathname2url() failed; %s != %s' % (expect, result))
