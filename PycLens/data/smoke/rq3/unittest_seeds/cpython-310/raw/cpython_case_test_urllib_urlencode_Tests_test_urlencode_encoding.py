# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_urlencode_encoding

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = (('\xa0', 'Á'),)
    expect = '%3F=%3F'
    result = urllib.parse.urlencode(given, encoding='ASCII', errors='replace')
    self.assertEqual(expect, result)
    given = (('\xa0', 'Á'),)
    expect = '%C2%A0=%C3%81'
    result = urllib.parse.urlencode(given)
    self.assertEqual(expect, result)
    given = (('\xa0', 'Á'),)
    expect = '%A0=%C1'
    result = urllib.parse.urlencode(given, encoding='latin-1')
    self.assertEqual(expect, result)
