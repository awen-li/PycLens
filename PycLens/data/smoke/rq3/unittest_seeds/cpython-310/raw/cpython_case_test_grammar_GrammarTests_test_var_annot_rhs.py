# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_rhs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    ns = {}
    exec('x: tuple = 1, 2', ns)
    self.assertEqual(ns['x'], (1, 2))
    stmt = 'def f():\n    x: int = yield'
    exec(stmt, ns)
    self.assertEqual(list(ns['f']()), [None])
    ns = {'a': 1, 'b': (2, 3, 4), 'c': 5, 'Tuple': typing.Tuple}
    exec('x: Tuple[int, ...] = a,*b,c', ns)
    self.assertEqual(ns['x'], (1, 2, 3, 4, 5))
