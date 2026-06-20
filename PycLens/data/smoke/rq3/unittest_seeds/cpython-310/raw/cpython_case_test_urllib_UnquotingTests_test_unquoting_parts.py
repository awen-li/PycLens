# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: UnquotingTests_test_unquoting_parts

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = 'ab%sd' % hexescape('c')
    expect = 'abcd'
    result = urllib.parse.unquote(given)
    self.assertEqual(expect, result, 'using quote(): %r != %r' % (expect, result))
    result = urllib.parse.unquote_plus(given)
    self.assertEqual(expect, result, 'using unquote_plus(): %r != %r' % (expect, result))
