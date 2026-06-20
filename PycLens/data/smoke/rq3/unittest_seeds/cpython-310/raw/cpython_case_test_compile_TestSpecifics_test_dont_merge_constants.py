# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_dont_merge_constants

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def check_different_constants(const1, const2):
        ns = {}
        exec('f1, f2 = lambda: %r, lambda: %r' % (const1, const2), ns)
        f1 = ns['f1']
        f2 = ns['f2']
        self.assertIsNot(f1.__code__, f2.__code__)
        self.assertNotEqual(f1.__code__, f2.__code__)
        self.check_constant(f1, const1)
        self.check_constant(f2, const2)
        self.assertEqual(repr(f1()), repr(const1))
        self.assertEqual(repr(f2()), repr(const2))
    check_different_constants(0, 0.0)
    check_different_constants(+0.0, -0.0)
    check_different_constants((0,), (0.0,))
    check_different_constants('a', b'a')
    check_different_constants(('a',), (b'a',))
    (f1, f2) = (lambda : +0j, lambda : -0j)
    self.assertIsNot(f1.__code__, f2.__code__)
    self.check_constant(f1, +0j)
    self.check_constant(f2, -0j)
    self.assertEqual(repr(f1()), repr(+0j))
    self.assertEqual(repr(f2()), repr(-0j))
    (f1, f2) = (lambda x: x in {0}, lambda x: x in {0.0})
    self.assertIsNot(f1.__code__, f2.__code__)
    self.check_constant(f1, frozenset({0}))
    self.check_constant(f2, frozenset({0.0}))
    self.assertTrue(f1(0))
    self.assertTrue(f2(0.0))
