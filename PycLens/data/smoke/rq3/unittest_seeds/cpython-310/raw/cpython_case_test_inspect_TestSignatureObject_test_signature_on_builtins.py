# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_builtins

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi

    def test_unbound_method(o):
        """Use this to test unbound methods (things that should have a self)"""
        signature = inspect.signature(o)
        self.assertTrue(isinstance(signature, inspect.Signature))
        self.assertEqual(list(signature.parameters.values())[0].name, 'self')
        return signature

    def test_callable(o):
        """Use this to test bound methods or normal callables (things that don't expect self)"""
        signature = inspect.signature(o)
        self.assertTrue(isinstance(signature, inspect.Signature))
        if signature.parameters:
            self.assertNotEqual(list(signature.parameters.values())[0].name, 'self')
        return signature
    signature = test_callable(_testcapi.docstring_with_signature_with_defaults)

    def p(name):
        return signature.parameters[name].default
    self.assertEqual(p('s'), 'avocado')
    self.assertEqual(p('b'), b'bytes')
    self.assertEqual(p('d'), 3.14)
    self.assertEqual(p('i'), 35)
    self.assertEqual(p('n'), None)
    self.assertEqual(p('t'), True)
    self.assertEqual(p('f'), False)
    self.assertEqual(p('local'), 3)
    self.assertEqual(p('sys'), sys.maxsize)
    self.assertEqual(p('exp'), sys.maxsize - 1)
    test_callable(object)
    test_unbound_method(_pickle.Pickler.dump)
    d = _pickle.Pickler(io.StringIO())
    test_callable(d.dump)
    test_callable(bytes.maketrans)
    test_callable(b'abc'.maketrans)
    test_callable(dict.fromkeys)
    test_callable({}.fromkeys)
    test_unbound_method(type.__call__)
    test_unbound_method(int.__add__)
    test_callable(3 .__add__)
    test_callable(min.__call__)
    with self.assertRaisesRegex(ValueError, 'no signature found'):

        class ThisWorksNow:
            __call__ = type
        test_callable(ThisWorksNow())
    test_unbound_method(dict.__delitem__)
    test_unbound_method(property.__delete__)
    test_callable(_testcapi.docstring_with_signature_but_no_doc)
