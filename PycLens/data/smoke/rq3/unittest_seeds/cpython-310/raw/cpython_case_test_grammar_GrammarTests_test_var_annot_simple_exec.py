# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_grammar.py
# case: GrammarTests_test_var_annot_simple_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    gns = {}
    lns = {}
    exec("'docstring'\n__annotations__[1] = 2\nx: int = 5\n", gns, lns)
    self.assertEqual(lns['__annotations__'], {1: 2, 'x': int})
    with self.assertRaises(KeyError):
        gns['__annotations__']
