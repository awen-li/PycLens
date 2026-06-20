# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_re.py
# case: ReTests_test_special_escapes

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertEqual(re.search('\\b(b.)\\b', 'abcd abc bcd bx').group(1), 'bx')
    self.assertEqual(re.search('\\B(b.)\\B', 'abc bcd bc abxd').group(1), 'bx')
    self.assertEqual(re.search('\\b(b.)\\b', 'abcd abc bcd bx', re.ASCII).group(1), 'bx')
    self.assertEqual(re.search('\\B(b.)\\B', 'abc bcd bc abxd', re.ASCII).group(1), 'bx')
    self.assertEqual(re.search('^abc$', '\nabc\n', re.M).group(0), 'abc')
    self.assertEqual(re.search('^\\Aabc\\Z$', 'abc', re.M).group(0), 'abc')
    self.assertIsNone(re.search('^\\Aabc\\Z$', '\nabc\n', re.M))
    self.assertEqual(re.search(b'\\b(b.)\\b', b'abcd abc bcd bx').group(1), b'bx')
    self.assertEqual(re.search(b'\\B(b.)\\B', b'abc bcd bc abxd').group(1), b'bx')
    self.assertEqual(re.search(b'\\b(b.)\\b', b'abcd abc bcd bx', re.LOCALE).group(1), b'bx')
    self.assertEqual(re.search(b'\\B(b.)\\B', b'abc bcd bc abxd', re.LOCALE).group(1), b'bx')
    self.assertEqual(re.search(b'^abc$', b'\nabc\n', re.M).group(0), b'abc')
    self.assertEqual(re.search(b'^\\Aabc\\Z$', b'abc', re.M).group(0), b'abc')
    self.assertIsNone(re.search(b'^\\Aabc\\Z$', b'\nabc\n', re.M))
    self.assertEqual(re.search('\\d\\D\\w\\W\\s\\S', '1aa! a').group(0), '1aa! a')
    self.assertEqual(re.search(b'\\d\\D\\w\\W\\s\\S', b'1aa! a').group(0), b'1aa! a')
    self.assertEqual(re.search('\\d\\D\\w\\W\\s\\S', '1aa! a', re.ASCII).group(0), '1aa! a')
    self.assertEqual(re.search(b'\\d\\D\\w\\W\\s\\S', b'1aa! a', re.LOCALE).group(0), b'1aa! a')
