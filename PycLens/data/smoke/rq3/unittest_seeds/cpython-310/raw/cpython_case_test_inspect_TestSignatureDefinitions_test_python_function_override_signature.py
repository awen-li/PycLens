# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureDefinitions_test_python_function_override_signature

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def func(*args, **kwargs):
        pass
    func.__text_signature__ = '($self, a, b=1, *args, c, d=2, **kwargs)'
    sig = inspect.signature(func)
    self.assertIsNotNone(sig)
    self.assertEqual(str(sig), '(self, /, a, b=1, *args, c, d=2, **kwargs)')
    func.__text_signature__ = '($self, a, b=1, /, *args, c, d=2, **kwargs)'
    sig = inspect.signature(func)
    self.assertEqual(str(sig), '(self, a, b=1, /, *args, c, d=2, **kwargs)')
    func.__text_signature__ = '(self, a=1+2, b=4-3, c=1 | 3 | 16)'
    sig = inspect.signature(func)
    self.assertEqual(str(sig), '(self, a=3, b=1, c=19)')
    func.__text_signature__ = '(self, a=1,\nb=2,\n\n\n   c=3)'
    sig = inspect.signature(func)
    self.assertEqual(str(sig), '(self, a=1, b=2, c=3)')
    func.__text_signature__ = '(self, x=does_not_exist)'
    with self.assertRaises(ValueError):
        inspect.signature(func)
    func.__text_signature__ = '(self, x=sys, y=inspect)'
    with self.assertRaises(ValueError):
        inspect.signature(func)
    func.__text_signature__ = '(self, 123)'
    with self.assertRaises(ValueError):
        inspect.signature(func)
