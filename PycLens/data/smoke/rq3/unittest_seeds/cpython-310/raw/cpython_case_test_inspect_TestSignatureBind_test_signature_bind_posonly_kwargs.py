# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_posonly_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def foo(bar, /, **kwargs):
        return (bar, kwargs.get(bar))
    sig = inspect.signature(foo)
    result = sig.bind('pos-only', bar='keyword')
    self.assertEqual(result.kwargs, {'bar': 'keyword'})
    self.assertIn(('bar', 'pos-only'), result.arguments.items())
