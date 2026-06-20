# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_object

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    S = inspect.Signature
    P = inspect.Parameter
    self.assertEqual(str(S()), '()')
    self.assertEqual(repr(S().parameters), 'mappingproxy(OrderedDict())')

    def test(po, pk, pod=42, pkd=100, *args, ko, **kwargs):
        pass
    sig = inspect.signature(test)
    po = sig.parameters['po'].replace(kind=P.POSITIONAL_ONLY)
    pod = sig.parameters['pod'].replace(kind=P.POSITIONAL_ONLY)
    pk = sig.parameters['pk']
    pkd = sig.parameters['pkd']
    args = sig.parameters['args']
    ko = sig.parameters['ko']
    kwargs = sig.parameters['kwargs']
    S((po, pk, args, ko, kwargs))
    with self.assertRaisesRegex(ValueError, 'wrong parameter order'):
        S((pk, po, args, ko, kwargs))
    with self.assertRaisesRegex(ValueError, 'wrong parameter order'):
        S((po, args, pk, ko, kwargs))
    with self.assertRaisesRegex(ValueError, 'wrong parameter order'):
        S((args, po, pk, ko, kwargs))
    with self.assertRaisesRegex(ValueError, 'wrong parameter order'):
        S((po, pk, args, kwargs, ko))
    kwargs2 = kwargs.replace(name='args')
    with self.assertRaisesRegex(ValueError, 'duplicate parameter name'):
        S((po, pk, args, kwargs2, ko))
    with self.assertRaisesRegex(ValueError, 'follows default argument'):
        S((pod, po))
    with self.assertRaisesRegex(ValueError, 'follows default argument'):
        S((po, pkd, pk))
    with self.assertRaisesRegex(ValueError, 'follows default argument'):
        S((pkd, pk))
    self.assertTrue(repr(sig).startswith('<Signature'))
    self.assertTrue('(po, pk' in repr(sig))
