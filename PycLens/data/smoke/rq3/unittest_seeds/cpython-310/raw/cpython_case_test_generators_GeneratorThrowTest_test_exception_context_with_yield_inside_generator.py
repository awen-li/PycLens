# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorThrowTest_test_exception_context_with_yield_inside_generator

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def f():
        try:
            raise KeyError('a')
        except Exception:
            try:
                yield
            except Exception as exc:
                self.assertEqual(type(exc), ValueError)
                context = exc.__context__
                self.assertEqual((type(context), context.args), (KeyError, ('a',)))
                yield 'b'
    gen = f()
    gen.send(None)
    actual = gen.throw(ValueError)
    self.assertEqual(actual, 'b')
