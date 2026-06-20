# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_args_and_varargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, b, c=3, *args):
        return (a, b, c, args)
    self.assertEqual(self.call(test, 1, 2, 3, 4, 5), (1, 2, 3, (4, 5)))
    self.assertEqual(self.call(test, 1, 2), (1, 2, 3, ()))
    self.assertEqual(self.call(test, b=1, a=2), (2, 1, 3, ()))
    self.assertEqual(self.call(test, 1, b=2), (1, 2, 3, ()))
    with self.assertRaisesRegex(TypeError, "multiple values for argument 'c'"):
        self.call(test, 1, 2, 3, c=4)
