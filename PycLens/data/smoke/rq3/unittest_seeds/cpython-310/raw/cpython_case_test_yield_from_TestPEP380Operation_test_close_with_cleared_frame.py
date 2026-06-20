# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_yield_from.py
# case: TestPEP380Operation_test_close_with_cleared_frame

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def innermost():
        yield

    def inner():
        outer_gen = (yield)
        yield from innermost()

    def outer():
        inner_gen = (yield)
        yield from inner_gen
    with disable_gc():
        inner_gen = inner()
        outer_gen = outer()
        outer_gen.send(None)
        outer_gen.send(inner_gen)
        outer_gen.send(outer_gen)
        del outer_gen
        del inner_gen
        gc_collect()
