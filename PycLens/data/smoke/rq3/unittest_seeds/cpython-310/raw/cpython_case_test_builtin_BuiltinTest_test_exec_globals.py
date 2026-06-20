# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_exec_globals

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    code = compile("print('Hello World!')", '', 'exec')
    self.assertRaisesRegex(NameError, "name 'print' is not defined", exec, code, {'__builtins__': {}})
    self.assertRaises(TypeError, exec, code, {'__builtins__': 123})
    code = compile('class A: pass', '', 'exec')
    self.assertRaisesRegex(NameError, '__build_class__ not found', exec, code, {'__builtins__': {}})

    class frozendict_error(Exception):
        pass

    class frozendict(dict):

        def __setitem__(self, key, value):
            raise frozendict_error('frozendict is readonly')
    if isinstance(__builtins__, types.ModuleType):
        frozen_builtins = frozendict(__builtins__.__dict__)
    else:
        frozen_builtins = frozendict(__builtins__)
    code = compile("__builtins__['superglobal']=2; print(superglobal)", 'test', 'exec')
    self.assertRaises(frozendict_error, exec, code, {'__builtins__': frozen_builtins})
    namespace = frozendict({})
    code = compile('x=1', 'test', 'exec')
    self.assertRaises(frozendict_error, exec, code, namespace)
