# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_unicode.py
# case: UnicodeTest_test_join

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    string_tests.MixinStrUnicodeUserStringTest.test_join(self)

    class MyWrapper:

        def __init__(self, sval):
            self.sval = sval

        def __str__(self):
            return self.sval
    self.checkequalnofix('a b c d', ' ', 'join', ['a', 'b', 'c', 'd'])
    self.checkequalnofix('abcd', '', 'join', ('a', 'b', 'c', 'd'))
    self.checkequalnofix('w x y z', ' ', 'join', string_tests.Sequence('wxyz'))
    self.checkequalnofix('a b c d', ' ', 'join', ['a', 'b', 'c', 'd'])
    self.checkequalnofix('a b c d', ' ', 'join', ['a', 'b', 'c', 'd'])
    self.checkequalnofix('abcd', '', 'join', ('a', 'b', 'c', 'd'))
    self.checkequalnofix('w x y z', ' ', 'join', string_tests.Sequence('wxyz'))
    self.checkraises(TypeError, ' ', 'join', ['1', '2', MyWrapper('foo')])
    self.checkraises(TypeError, ' ', 'join', ['1', '2', '3', bytes()])
    self.checkraises(TypeError, ' ', 'join', [1, 2, 3])
    self.checkraises(TypeError, ' ', 'join', ['1', '2', 3])
