# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_partition

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.MixinStrUnicodeUserStringTest.test_partition(self)
    self.checkequal(('ABCDEFGH', '', ''), 'ABCDEFGH', 'partition', '䈀')
    for (left, right) in ('ba', 'āĀ', '𐌁𐌀'):
        left *= 9
        right *= 9
        for delim in ('c', 'Ă', '𐌂'):
            self.checkequal((left + right, '', ''), left + right, 'partition', delim)
            self.checkequal((left, delim, right), left + delim + right, 'partition', delim)
            self.checkequal((left + right, '', ''), left + right, 'partition', delim * 2)
            self.checkequal((left, delim * 2, right), left + delim * 2 + right, 'partition', delim * 2)
