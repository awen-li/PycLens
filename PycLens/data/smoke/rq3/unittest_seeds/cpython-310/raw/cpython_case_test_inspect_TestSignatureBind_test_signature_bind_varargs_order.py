# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_varargs_order

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(*args):
        return args
    self.assertEqual(self.call(test), ())
    self.assertEqual(self.call(test, 1, 2, 3), (1, 2, 3))
