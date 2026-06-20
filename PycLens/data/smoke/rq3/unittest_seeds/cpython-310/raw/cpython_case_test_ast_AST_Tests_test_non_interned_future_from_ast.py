# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: AST_Tests_test_non_interned_future_from_ast

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    mod = ast.parse('from __future__ import division')
    self.assertIsInstance(mod.body[0], ast.ImportFrom)
    mod.body[0].module = ' __future__ '.strip()
    compile(mod, '<test>', 'exec')
