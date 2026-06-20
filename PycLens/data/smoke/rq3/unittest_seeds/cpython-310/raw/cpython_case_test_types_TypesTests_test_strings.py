# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_types.py
# case: TypesTests_test_strings

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    if len('') != 0:
        self.fail("len('')")
    if len('a') != 1:
        self.fail("len('a')")
    if len('abcdef') != 6:
        self.fail("len('abcdef')")
    if 'xyz' + 'abcde' != 'xyzabcde':
        self.fail('string concatenation')
    if 'xyz' * 3 != 'xyzxyzxyz':
        self.fail('string repetition *3')
    if 0 * 'abcde' != '':
        self.fail('string repetition 0*')
    if min('abc') != 'a' or max('abc') != 'c':
        self.fail('min/max string')
    if 'a' in 'abc' and 'b' in 'abc' and ('c' in 'abc') and ('d' not in 'abc'):
        pass
    else:
        self.fail('in/not in string')
    x = 'x' * 103
    if '%s!' % x != x + '!':
        self.fail('nasty string formatting bug')
    a = '0123456789'
    self.assertEqual(a[:], a)
    self.assertEqual(a[::2], '02468')
    self.assertEqual(a[1::2], '13579')
    self.assertEqual(a[::-1], '9876543210')
    self.assertEqual(a[::-2], '97531')
    self.assertEqual(a[3::-2], '31')
    self.assertEqual(a[-100:100], a)
    self.assertEqual(a[100:-100:-1], a[::-1])
    self.assertEqual(a[-100:100:2], '02468')
