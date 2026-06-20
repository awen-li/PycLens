# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_genexps

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = ([x for x in range(10)] for x in range(1))
    self.assertEqual(next(g), [x for x in range(10)])
    try:
        next(g)
        self.fail('should produce StopIteration exception')
    except StopIteration:
        pass
    a = 1
    try:
        g = (a for d in a)
        next(g)
        self.fail('should produce TypeError')
    except TypeError:
        pass
    self.assertEqual(list(((x, y) for x in 'abcd' for y in 'abcd')), [(x, y) for x in 'abcd' for y in 'abcd'])
    self.assertEqual(list(((x, y) for x in 'ab' for y in 'xy')), [(x, y) for x in 'ab' for y in 'xy'])
    a = [x for x in range(10)]
    b = (x for x in (y for y in a))
    self.assertEqual(sum(b), sum([x for x in range(10)]))
    self.assertEqual(sum((x ** 2 for x in range(10))), sum([x ** 2 for x in range(10)]))
    self.assertEqual(sum((x * x for x in range(10) if x % 2)), sum([x * x for x in range(10) if x % 2]))
    self.assertEqual(sum((x for x in (y for y in range(10)))), sum([x for x in range(10)]))
    self.assertEqual(sum((x for x in (y for y in (z for z in range(10))))), sum([x for x in range(10)]))
    self.assertEqual(sum((x for x in [y for y in (z for z in range(10))])), sum([x for x in range(10)]))
    self.assertEqual(sum((x for x in (y for y in (z for z in range(10) if True)) if True)), sum([x for x in range(10)]))
    self.assertEqual(sum((x for x in (y for y in (z for z in range(10) if True) if False) if True)), 0)
    check_syntax_error(self, 'foo(x for x in range(10), 100)')
    check_syntax_error(self, 'foo(100, x for x in range(10))')
