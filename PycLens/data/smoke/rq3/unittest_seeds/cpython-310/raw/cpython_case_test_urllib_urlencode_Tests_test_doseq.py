# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_doseq

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = {'sequence': ['1', '2', '3']}
    expect = 'sequence=%s' % urllib.parse.quote_plus(str(['1', '2', '3']))
    result = urllib.parse.urlencode(given)
    self.assertEqual(expect, result)
    result = urllib.parse.urlencode(given, True)
    for value in given['sequence']:
        expect = 'sequence=%s' % value
        self.assertIn(expect, result)
    self.assertEqual(result.count('&'), 2, "Expected 2 '&'s, got %s" % result.count('&'))
