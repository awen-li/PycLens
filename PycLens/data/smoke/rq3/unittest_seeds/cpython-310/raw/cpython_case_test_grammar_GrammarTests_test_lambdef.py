# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_lambdef

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    l1 = lambda : 0
    self.assertEqual(l1(), 0)
    l2 = lambda : a[d]
    l3 = lambda : [2 < x for x in [-1, 3, 0]]
    self.assertEqual(l3(), [0, 1, 0])
    l4 = lambda x=lambda y=lambda z=1: z: y(): x()
    self.assertEqual(l4(), 1)
    l5 = lambda x, y, z=2: x + y + z
    self.assertEqual(l5(1, 2), 5)
    self.assertEqual(l5(1, 2, 3), 6)
    check_syntax_error(self, 'lambda x: x = 2')
    check_syntax_error(self, 'lambda (None,): None')
    l6 = lambda x, y, *, k=20: x + y + k
    self.assertEqual(l6(1, 2), 1 + 2 + 20)
    self.assertEqual(l6(1, 2, k=10), 1 + 2 + 10)
    l10 = lambda a: 0
    l11 = lambda *args: 0
    l12 = lambda **kwds: 0
    l13 = lambda a, *args: 0
    l14 = lambda a, **kwds: 0
    l15 = lambda *args, b: 0
    l16 = lambda *, b: 0
    l17 = lambda *args, **kwds: 0
    l18 = lambda a, *args, b: 0
    l19 = lambda a, *, b: 0
    l20 = lambda a, *args, **kwds: 0
    l21 = lambda *args, b, **kwds: 0
    l22 = lambda *, b, **kwds: 0
    l23 = lambda a, *args, b, **kwds: 0
    l24 = lambda a, *, b, **kwds: 0
