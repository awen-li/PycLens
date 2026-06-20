# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_exceptions.py
# case: ExceptionTests_test_generator_finalizing_and_exc_info

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def simple_gen():
        yield 1

    def run_gen():
        gen = simple_gen()
        try:
            raise RuntimeError
        except RuntimeError:
            return next(gen)
    run_gen()
    gc_collect()
    self.assertEqual(sys.exc_info(), (None, None, None))
