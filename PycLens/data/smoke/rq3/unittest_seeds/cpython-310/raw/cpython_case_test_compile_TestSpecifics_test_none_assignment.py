# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_none_assignment

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stmts = ['None = 0', 'None += 0', '__builtins__.None = 0', 'def None(): pass', 'class None: pass', '(a, None) = 0, 0', 'for None in range(10): pass', 'def f(None): pass', 'import None', 'import x as None', 'from x import None', 'from x import y as None']
    for stmt in stmts:
        stmt += '\n'
        self.assertRaises(SyntaxError, compile, stmt, 'tmp', 'single')
        self.assertRaises(SyntaxError, compile, stmt, 'tmp', 'exec')
