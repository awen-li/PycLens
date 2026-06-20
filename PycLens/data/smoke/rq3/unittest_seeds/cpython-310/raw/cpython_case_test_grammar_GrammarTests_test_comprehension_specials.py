# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_comprehension_specials

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    x = 10
    g = (i for i in range(x))
    x = 5
    self.assertEqual(len(list(g)), 10)
    x = 10
    t = False
    g = ((i, j) for i in range(x) if t for j in range(x))
    x = 5
    t = True
    self.assertEqual([(i, j) for i in range(10) for j in range(5)], list(g))
    self.assertEqual([x for x in range(10) if x % 2 if x % 3], [1, 5, 7])
    self.assertEqual(list((x for x in range(10) if x % 2 if x % 3)), [1, 5, 7])
    self.assertEqual([x for (x,) in [(4,), (5,), (6,)]], [4, 5, 6])
    self.assertEqual(list((x for (x,) in [(7,), (8,), (9,)])), [7, 8, 9])
