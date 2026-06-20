# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_contextlib.py
# case: ContextManagerTestCase_test_param_errors

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    @contextmanager
    def woohoo(a, *, b):
        yield
    with self.assertRaises(TypeError):
        woohoo()
    with self.assertRaises(TypeError):
        woohoo(3, 5)
    with self.assertRaises(TypeError):
        woohoo(b=3)
