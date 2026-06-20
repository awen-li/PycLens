# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_stopiteration_error

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        raise StopIteration
        yield
    with self.assertRaisesRegex(RuntimeError, 'raised StopIteration'):
        next(gen())
