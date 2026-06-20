# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_positional_only

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    P = inspect.Parameter

    def test(a_po, b_po, c_po=3, foo=42, *, bar=50, **kwargs):
        return (a_po, b_po, c_po, foo, bar, kwargs)
    sig = inspect.signature(test)
    new_params = collections.OrderedDict(tuple(sig.parameters.items()))
    for name in ('a_po', 'b_po', 'c_po'):
        new_params[name] = new_params[name].replace(kind=P.POSITIONAL_ONLY)
    new_sig = sig.replace(parameters=new_params.values())
    test.__signature__ = new_sig
    self.assertEqual(self.call(test, 1, 2, 4, 5, bar=6), (1, 2, 4, 5, 6, {}))
    self.assertEqual(self.call(test, 1, 2), (1, 2, 3, 42, 50, {}))
    self.assertEqual(self.call(test, 1, 2, foo=4, bar=5), (1, 2, 3, 4, 5, {}))
    with self.assertRaisesRegex(TypeError, 'but was passed as a keyword'):
        self.call(test, 1, 2, foo=4, bar=5, c_po=10)
    with self.assertRaisesRegex(TypeError, 'parameter is positional only'):
        self.call(test, 1, 2, c_po=4)
    with self.assertRaisesRegex(TypeError, 'parameter is positional only'):
        self.call(test, a_po=1, b_po=2)
