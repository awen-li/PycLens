# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: Pathname_Tests_test_quoting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = os.path.join('needs', 'quot=ing', 'here')
    expect = 'needs/%s/here' % urllib.parse.quote('quot=ing')
    result = urllib.request.pathname2url(given)
    self.assertEqual(expect, result, 'pathname2url() failed; %s != %s' % (expect, result))
    expect = given
    result = urllib.request.url2pathname(result)
    self.assertEqual(expect, result, 'url2pathname() failed; %s != %s' % (expect, result))
    given = os.path.join('make sure', 'using_quote')
    expect = '%s/using_quote' % urllib.parse.quote('make sure')
    result = urllib.request.pathname2url(given)
    self.assertEqual(expect, result, 'pathname2url() failed; %s != %s' % (expect, result))
    given = 'make+sure/using_unquote'
    expect = os.path.join('make+sure', 'using_unquote')
    result = urllib.request.url2pathname(given)
    self.assertEqual(expect, result, 'url2pathname() failed; %s != %s' % (expect, result))
