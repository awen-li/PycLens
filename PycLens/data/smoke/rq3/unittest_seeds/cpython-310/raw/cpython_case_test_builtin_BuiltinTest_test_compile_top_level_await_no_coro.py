# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_builtin.py
# case: BuiltinTest_test_compile_top_level_await_no_coro

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    modes = ('single', 'exec')
    code_samples = ['def f():pass\n', '[x for x in l]', '{x for x in l}', '(x for x in l)', '{x:x for x in l}']
    for (mode, code_sample) in product(modes, code_samples):
        source = dedent(code_sample)
        co = compile(source, '?', mode, flags=ast.PyCF_ALLOW_TOP_LEVEL_AWAIT)
        self.assertNotEqual(co.co_flags & CO_COROUTINE, CO_COROUTINE, msg=f'source={source} mode={mode}')
