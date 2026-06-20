# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_contains

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    self.assertIn('a', 'abdb')
    self.assertIn('a', 'bdab')
    self.assertIn('a', 'bdaba')
    self.assertIn('a', 'bdba')
    self.assertNotIn('a', 'bdb')
    self.assertIn('a', 'bdba')
    self.assertIn('a', ('a', 1, None))
    self.assertIn('a', (1, None, 'a'))
    self.assertIn('a', ('a', 1, None))
    self.assertIn('a', (1, None, 'a'))
    self.assertNotIn('a', ('x', 1, 'y'))
    self.assertNotIn('a', ('x', 1, None))
    self.assertNotIn('abcd', 'abcxxxx')
    self.assertIn('ab', 'abcd')
    self.assertIn('ab', 'abc')
    self.assertIn('ab', (1, None, 'ab'))
    self.assertIn('', 'abc')
    self.assertIn('', '')
    self.assertIn('', 'abc')
    self.assertNotIn('\x00', 'abc')
    self.assertIn('\x00', '\x00abc')
    self.assertIn('\x00', 'abc\x00')
    self.assertIn('a', '\x00abc')
    self.assertIn('asdf', 'asdf')
    self.assertNotIn('asdf', 'asd')
    self.assertNotIn('asdf', '')
    self.assertRaises(TypeError, 'abc'.__contains__)
    for fill in ('a', 'Ā', '𐌀'):
        fill *= 9
        for delim in ('c', 'Ă', '𐌂'):
            self.assertNotIn(delim, fill)
            self.assertIn(delim, fill + delim)
            self.assertNotIn(delim * 2, fill)
            self.assertIn(delim * 2, fill + delim * 2)
