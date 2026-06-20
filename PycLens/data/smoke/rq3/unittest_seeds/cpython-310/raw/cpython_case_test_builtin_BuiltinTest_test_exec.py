# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    g = {}
    exec('z = 1', g)
    if '__builtins__' in g:
        del g['__builtins__']
    self.assertEqual(g, {'z': 1})
    exec('z = 1+1', g)
    if '__builtins__' in g:
        del g['__builtins__']
    self.assertEqual(g, {'z': 2})
    g = {}
    l = {}
    with check_warnings():
        warnings.filterwarnings('ignore', 'global statement', module='<string>')
        exec('global a; a = 1; b = 2', g, l)
    if '__builtins__' in g:
        del g['__builtins__']
    if '__builtins__' in l:
        del l['__builtins__']
    self.assertEqual((g, l), ({'a': 1}, {'b': 2}))
