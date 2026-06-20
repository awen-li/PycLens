# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_vararg_name

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, *args):
        return (a, args)
    sig = inspect.signature(test)
    with self.assertRaisesRegex(TypeError, "got an unexpected keyword argument 'args'"):
        sig.bind(a=0, args=1)

    def test(*args, **kwargs):
        return (args, kwargs)
    self.assertEqual(self.call(test, args=1), ((), {'args': 1}))
    sig = inspect.signature(test)
    ba = sig.bind(args=1)
    self.assertEqual(ba.arguments, {'kwargs': {'args': 1}})
