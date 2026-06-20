# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_generators.py
# case: ExceptionTest_test_except_throw_bad_exception

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class E(Exception):

        def __new__(cls, *args, **kwargs):
            return cls

    def boring_generator():
        yield
    gen = boring_generator()
    err_msg = 'should have returned an instance of BaseException'
    with self.assertRaisesRegex(TypeError, err_msg):
        gen.throw(E)
    self.assertRaises(StopIteration, next, gen)

    def generator():
        with self.assertRaisesRegex(TypeError, err_msg):
            yield
    gen = generator()
    next(gen)
    with self.assertRaises(StopIteration):
        gen.throw(E)
