# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_builtins_no_signature

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    import _testcapi
    with self.assertRaisesRegex(ValueError, 'no signature found for builtin'):
        inspect.signature(_testcapi.docstring_no_signature)
    with self.assertRaisesRegex(ValueError, 'no signature found for builtin'):
        inspect.signature(str)
