# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_urlencode_bytes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = ((b'\xa0$', b'\xc1$'),)
    expect = '%A0%24=%C1%24'
    result = urllib.parse.urlencode(given)
    self.assertEqual(expect, result)
    result = urllib.parse.urlencode(given, True)
    self.assertEqual(expect, result)
    given = ((b'\xa0$', (42, b'\xc1$')),)
    expect = '%A0%24=42&%A0%24=%C1%24'
    result = urllib.parse.urlencode(given, True)
    self.assertEqual(expect, result)
