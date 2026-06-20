# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: GeneratorStackTraceTest_test_throw_with_yield_from

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def call_throw(gen):
        gen.throw(RuntimeError)
    self.check_yield_from_example(call_throw)
