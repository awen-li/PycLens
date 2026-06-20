# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_code.py
# case: CodeTest_test_replace

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func():
        x = 1
        return x
    code = func.__code__

    def func2():
        y = 2
        return y
    code2 = func2.__code__
    for (attr, value) in (('co_argcount', 0), ('co_posonlyargcount', 0), ('co_kwonlyargcount', 0), ('co_nlocals', 0), ('co_stacksize', 0), ('co_flags', code.co_flags | inspect.CO_COROUTINE), ('co_firstlineno', 100), ('co_code', code2.co_code), ('co_consts', code2.co_consts), ('co_names', ('myname',)), ('co_varnames', code2.co_varnames), ('co_freevars', ('freevar',)), ('co_cellvars', ('cellvar',)), ('co_filename', 'newfilename'), ('co_name', 'newname'), ('co_linetable', code2.co_linetable)):
        with self.subTest(attr=attr, value=value):
            new_code = code.replace(**{attr: value})
            self.assertEqual(getattr(new_code, attr), value)
