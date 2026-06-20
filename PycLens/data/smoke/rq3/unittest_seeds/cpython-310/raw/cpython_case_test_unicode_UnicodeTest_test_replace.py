# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.CommonTest.test_replace(self)
    self.checkequalnofix('one@two!three!', 'one!two!three!', 'replace', '!', '@', 1)
    self.assertRaises(TypeError, 'replace'.replace, 'r', 42)
    for (left, right) in ('ba', 'āĀ', '𐌁𐌀'):
        left *= 9
        right *= 9
        for delim in ('c', 'Ă', '𐌂'):
            for repl in ('d', 'ă', '𐌃'):
                self.checkequal(left + right, left + right, 'replace', delim, repl)
                self.checkequal(left + repl + right, left + delim + right, 'replace', delim, repl)
                self.checkequal(left + right, left + right, 'replace', delim * 2, repl)
                self.checkequal(left + repl + right, left + delim * 2 + right, 'replace', delim * 2, repl)
