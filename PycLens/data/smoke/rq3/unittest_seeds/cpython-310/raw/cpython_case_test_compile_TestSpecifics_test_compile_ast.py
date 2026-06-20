# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_compile.py
# case: TestSpecifics_test_compile_ast

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    fname = __file__
    if fname.lower().endswith('pyc'):
        fname = fname[:-1]
    with open(fname, encoding='utf-8') as f:
        fcontents = f.read()
    sample_code = [['<assign>', 'x = 5'], ['<ifblock>', 'if True:\n    pass\n'], ['<forblock>', 'for n in [1, 2, 3]:\n    print(n)\n'], ['<deffunc>', 'def foo():\n    pass\nfoo()\n'], [fname, fcontents]]
    for (fname, code) in sample_code:
        co1 = compile(code, '%s1' % fname, 'exec')
        ast = compile(code, '%s2' % fname, 'exec', _ast.PyCF_ONLY_AST)
        self.assertTrue(type(ast) == _ast.Module)
        co2 = compile(ast, '%s3' % fname, 'exec')
        self.assertEqual(co1, co2)
        self.assertEqual(co2.co_filename, '%s3' % fname)
    co1 = compile('print(1)', '<string>', 'exec', _ast.PyCF_ONLY_AST)
    self.assertRaises(TypeError, compile, co1, '<ast>', 'eval')
    self.assertRaises(TypeError, compile, _ast.If(), '<ast>', 'exec')
    ast = _ast.Module()
    ast.body = [_ast.BoolOp()]
    self.assertRaises(TypeError, compile, ast, '<ast>', 'exec')
