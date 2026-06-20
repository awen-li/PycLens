# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorThrowTest_test_exception_context_with_yield

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        try:
            raise KeyError('a')
        except Exception:
            yield
    gen = f()
    gen.send(None)
    with self.assertRaises(ValueError) as cm:
        gen.throw(ValueError)
    context = cm.exception.__context__
    self.assertEqual((type(context), context.args), (KeyError, ('a',)))
