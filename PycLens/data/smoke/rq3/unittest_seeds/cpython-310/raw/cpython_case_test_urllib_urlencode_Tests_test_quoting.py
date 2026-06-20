# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_quoting

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = {'&': '='}
    expect = '%s=%s' % (hexescape('&'), hexescape('='))
    result = urllib.parse.urlencode(given)
    self.assertEqual(expect, result)
    given = {'key name': 'A bunch of pluses'}
    expect = 'key+name=A+bunch+of+pluses'
    result = urllib.parse.urlencode(given)
    self.assertEqual(expect, result)
