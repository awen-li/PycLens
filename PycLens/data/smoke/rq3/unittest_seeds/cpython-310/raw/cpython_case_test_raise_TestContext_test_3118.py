# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_raise.py
# case: TestContext_test_3118

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def gen():
        try:
            yield 1
        finally:
            pass

    def f():
        g = gen()
        next(g)
        try:
            try:
                raise ValueError
            except:
                del g
                raise KeyError
        except Exception as e:
            self.assertIsInstance(e.__context__, ValueError)
    f()
