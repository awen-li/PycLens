# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorThrowTest_test_exception_context_with_yield_from_with_context_cycle

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    has_cycle = None

    def f():
        yield

    def g(exc):
        nonlocal has_cycle
        try:
            raise exc
        except Exception:
            try:
                yield from f()
            except Exception as exc:
                has_cycle = exc is exc.__context__
        yield
    exc = KeyError('a')
    gen = g(exc)
    gen.send(None)
    gen.throw(exc)
    self.assertEqual(has_cycle, False)
