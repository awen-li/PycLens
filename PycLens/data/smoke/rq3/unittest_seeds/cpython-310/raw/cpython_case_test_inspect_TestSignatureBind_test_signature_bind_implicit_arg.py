# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_implicit_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def make_set():
        return {z * z for z in range(5)}
    setcomp_code = make_set.__code__.co_consts[1]
    setcomp_func = types.FunctionType(setcomp_code, {})
    iterator = iter(range(5))
    self.assertEqual(self.call(setcomp_func, iterator), {0, 1, 4, 9, 16})
