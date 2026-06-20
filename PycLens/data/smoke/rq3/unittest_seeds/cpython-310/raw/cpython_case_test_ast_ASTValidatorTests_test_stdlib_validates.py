# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_ast.py
# case: ASTValidatorTests_test_stdlib_validates

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    stdlib = os.path.dirname(ast.__file__)
    tests = [fn for fn in os.listdir(stdlib) if fn.endswith('.py')]
    tests.extend(['test/test_grammar.py', 'test/test_unpack_ex.py'])
    for module in tests:
        with self.subTest(module):
            fn = os.path.join(stdlib, module)
            with open(fn, 'r', encoding='utf-8') as fp:
                source = fp.read()
            mod = ast.parse(source, fn)
            compile(mod, fn, 'exec')
