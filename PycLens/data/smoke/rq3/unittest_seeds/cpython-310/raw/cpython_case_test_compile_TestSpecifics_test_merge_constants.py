# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_merge_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_same_constant(const):
        ns = {}
        code = 'f1, f2 = lambda: %r, lambda: %r' % (const, const)
        exec(code, ns)
        f1 = ns['f1']
        f2 = ns['f2']
        self.assertIs(f1.__code__, f2.__code__)
        self.check_constant(f1, const)
        self.assertEqual(repr(f1()), repr(const))
    check_same_constant(None)
    check_same_constant(0)
    check_same_constant(0.0)
    check_same_constant(b'abc')
    check_same_constant('abc')
    (f1, f2) = (lambda : ..., lambda : ...)
    self.assertIs(f1.__code__, f2.__code__)
    self.check_constant(f1, Ellipsis)
    self.assertEqual(repr(f1()), repr(Ellipsis))
    (f1, f2) = (lambda : 'not a name', lambda : ('not a name',))
    f3 = lambda x: x in {('not a name',)}
    self.assertIs(f1.__code__.co_consts[1], f2.__code__.co_consts[1][0])
    self.assertIs(next(iter(f3.__code__.co_consts[1])), f2.__code__.co_consts[1])
    (f1, f2) = (lambda x: x in {0}, lambda x: x in {0})
    self.assertIs(f1.__code__, f2.__code__)
    self.check_constant(f1, frozenset({0}))
    self.assertTrue(f1(0))
