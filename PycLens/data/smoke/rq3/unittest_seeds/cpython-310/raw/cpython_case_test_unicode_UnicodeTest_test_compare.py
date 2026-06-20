# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_compare

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    N = 10
    ascii = 'a' * N
    ascii2 = 'z' * N
    latin = '\x80' * N
    latin2 = 'ÿ' * N
    bmp = 'Ā' * N
    bmp2 = '\uffff' * N
    astral = '\U00100000' * N
    astral2 = '\U0010ffff' * N
    strings = (ascii, ascii2, latin, latin2, bmp, bmp2, astral, astral2)
    for (text1, text2) in itertools.combinations(strings, 2):
        equal = text1 is text2
        self.assertEqual(text1 == text2, equal)
        self.assertEqual(text1 != text2, not equal)
        if equal:
            self.assertTrue(text1 <= text2)
            self.assertTrue(text1 >= text2)
            copy1 = duplicate_string(text1)
            copy2 = duplicate_string(text2)
            self.assertIsNot(copy1, copy2)
            self.assertTrue(copy1 == copy2)
            self.assertFalse(copy1 != copy2)
            self.assertTrue(copy1 <= copy2)
            self.assertTrue(copy2 >= copy2)
    self.assertTrue(ascii < ascii2)
    self.assertTrue(ascii < latin)
    self.assertTrue(ascii < bmp)
    self.assertTrue(ascii < astral)
    self.assertFalse(ascii >= ascii2)
    self.assertFalse(ascii >= latin)
    self.assertFalse(ascii >= bmp)
    self.assertFalse(ascii >= astral)
    self.assertFalse(latin < ascii)
    self.assertTrue(latin < latin2)
    self.assertTrue(latin < bmp)
    self.assertTrue(latin < astral)
    self.assertTrue(latin >= ascii)
    self.assertFalse(latin >= latin2)
    self.assertFalse(latin >= bmp)
    self.assertFalse(latin >= astral)
    self.assertFalse(bmp < ascii)
    self.assertFalse(bmp < latin)
    self.assertTrue(bmp < bmp2)
    self.assertTrue(bmp < astral)
    self.assertTrue(bmp >= ascii)
    self.assertTrue(bmp >= latin)
    self.assertFalse(bmp >= bmp2)
    self.assertFalse(bmp >= astral)
    self.assertFalse(astral < ascii)
    self.assertFalse(astral < latin)
    self.assertFalse(astral < bmp2)
    self.assertTrue(astral < astral2)
    self.assertTrue(astral >= ascii)
    self.assertTrue(astral >= latin)
    self.assertTrue(astral >= bmp2)
    self.assertFalse(astral >= astral2)
