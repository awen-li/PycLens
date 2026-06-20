# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_decorators.py
# case: TestDecorators_test_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    for stmt in ('x,', 'x, y', 'x = y', 'pass', 'import sys'):
        compile(stmt, 'test', 'exec')
        with self.assertRaises(SyntaxError):
            compile(f'@{stmt}\ndef f(): pass', 'test', 'exec')
    for expr in ('1.+2j', '[1, 2][-1]', '(1, 2)', 'True', '...', 'None'):
        compile(expr, 'test', 'eval')
        with self.assertRaises(TypeError):
            exec(f'@{expr}\ndef f(): pass')

    def unimp(func):
        raise NotImplementedError
    context = dict(nullval=None, unimp=unimp)
    for (expr, exc) in [('undef', NameError), ('nullval', TypeError), ('nullval.attr', AttributeError), ('unimp', NotImplementedError)]:
        codestr = '@%s\ndef f(): pass\nassert f() is None' % expr
        code = compile(codestr, 'test', 'exec')
        self.assertRaises(exc, eval, code, context)
