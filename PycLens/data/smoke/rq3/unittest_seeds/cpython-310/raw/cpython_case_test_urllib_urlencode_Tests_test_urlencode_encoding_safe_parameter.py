# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_urllib.py
# case: urlencode_Tests_test_urlencode_encoding_safe_parameter

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    given = ((b'\xa0$', b'\xc1$'),)
    result = urllib.parse.urlencode(given, safe=':$')
    expect = '%A0$=%C1$'
    self.assertEqual(expect, result)
    given = ((b'\xa0$', b'\xc1$'),)
    result = urllib.parse.urlencode(given, doseq=True, safe=':$')
    expect = '%A0$=%C1$'
    self.assertEqual(expect, result)
    given = ((b'\xa0$', (b'\xc1$', 13, 42)),)
    expect = '%A0$=%C1$&%A0$=13&%A0$=42'
    result = urllib.parse.urlencode(given, True, safe=':$')
    self.assertEqual(expect, result)
    given = ((b'\xa0$', b'\xc1$'),)
    result = urllib.parse.urlencode(given, safe=':$', encoding='latin-1')
    expect = '%A0$=%C1$'
    self.assertEqual(expect, result)
    given = ((b'\xa0$', b'\xc1$'),)
    expect = '%A0$=%C1$'
    result = urllib.parse.urlencode(given, doseq=True, safe=':$', encoding='latin-1')
    given = ((b'\xa0$', (b'\xc1$', 13, 42)),)
    expect = '%A0$=%C1$&%A0$=13&%A0$=42'
    result = urllib.parse.urlencode(given, True, safe=':$', encoding='latin-1')
    self.assertEqual(expect, result)
