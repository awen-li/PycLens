# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_utf8source.py
# case: BuiltinCompileTests_test_latin1

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    source_code = '# coding: Latin-1\nu = "Ç"\n'.encode('Latin-1')
    try:
        code = compile(source_code, '<dummy>', 'exec')
    except SyntaxError:
        self.fail('compile() cannot handle Latin-1 source')
    ns = {}
    exec(code, ns)
    self.assertEqual('Ç', ns['u'])
