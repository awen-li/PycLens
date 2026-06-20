# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_just_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, b, c):
        return (a, b, c)
    self.assertEqual(self.call(test, 1, 2, 3), (1, 2, 3))
    with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
        self.call(test, 1, 2, 3, 4)
    with self.assertRaisesRegex(TypeError, "missing a required argument: 'b'"):
        self.call(test, 1)
    with self.assertRaisesRegex(TypeError, "missing a required argument: 'a'"):
        self.call(test)

    def test(a, b, c=10):
        return (a, b, c)
    self.assertEqual(self.call(test, 1, 2, 3), (1, 2, 3))
    self.assertEqual(self.call(test, 1, 2), (1, 2, 10))

    def test(a=1, b=2, c=3):
        return (a, b, c)
    self.assertEqual(self.call(test, a=10, c=13), (10, 2, 13))
    self.assertEqual(self.call(test, a=10), (10, 2, 3))
    self.assertEqual(self.call(test, b=10), (1, 10, 3))
