# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_dynamic.py
# case: RebindBuiltinsTests_test_cannot_change_globals_or_builtins_with_exec

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo():
        return len([1, 2, 3])
    self.configure_func(foo)
    globals_dict = {'foo': foo}
    exec('x = foo()', globals_dict)
    self.assertEqual(globals_dict['x'], 3)
    builtins_dict = {'len': lambda x: 7}
    globals_dict = {'foo': foo, '__builtins__': builtins_dict, 'len': lambda x: 8}
    exec('x = foo()', globals_dict)
    self.assertEqual(globals_dict['x'], 3)
