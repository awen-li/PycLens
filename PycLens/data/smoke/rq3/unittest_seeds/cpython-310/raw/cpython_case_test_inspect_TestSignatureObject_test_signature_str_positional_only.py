# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_str_positional_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = inspect.Parameter
    S = inspect.Signature

    def test(a_po, *, b, **kwargs):
        return (a_po, kwargs)
    sig = inspect.signature(test)
    new_params = list(sig.parameters.values())
    new_params[0] = new_params[0].replace(kind=P.POSITIONAL_ONLY)
    test.__signature__ = sig.replace(parameters=new_params)
    self.assertEqual(str(inspect.signature(test)), '(a_po, /, *, b, **kwargs)')
    self.assertEqual(str(S(parameters=[P('foo', P.POSITIONAL_ONLY)])), '(foo, /)')
    self.assertEqual(str(S(parameters=[P('foo', P.POSITIONAL_ONLY), P('bar', P.VAR_KEYWORD)])), '(foo, /, **bar)')
    self.assertEqual(str(S(parameters=[P('foo', P.POSITIONAL_ONLY), P('bar', P.VAR_POSITIONAL)])), '(foo, /, *bar)')
