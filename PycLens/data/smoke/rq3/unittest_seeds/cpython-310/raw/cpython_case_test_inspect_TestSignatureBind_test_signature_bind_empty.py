# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_empty

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test():
        return 42
    self.assertEqual(self.call(test), 42)
    with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
        self.call(test, 1)
    with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
        self.call(test, 1, spam=10)
    with self.assertRaisesRegex(TypeError, "got an unexpected keyword argument 'spam'"):
        self.call(test, spam=1)
