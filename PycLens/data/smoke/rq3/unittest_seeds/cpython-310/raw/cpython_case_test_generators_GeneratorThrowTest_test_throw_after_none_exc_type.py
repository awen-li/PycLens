# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorThrowTest_test_throw_after_none_exc_type

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def g():
        try:
            raise KeyError
        except KeyError:
            pass
        try:
            yield
        except Exception:
            raise RuntimeError
    gen = g()
    gen.send(None)
    with self.assertRaises(RuntimeError) as cm:
        gen.throw(ValueError)
