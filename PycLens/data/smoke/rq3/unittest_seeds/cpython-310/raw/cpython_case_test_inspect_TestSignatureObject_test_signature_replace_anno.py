# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_replace_anno

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test() -> 42:
        pass
    sig = inspect.signature(test)
    sig = sig.replace(return_annotation=None)
    self.assertIs(sig.return_annotation, None)
    sig = sig.replace(return_annotation=sig.empty)
    self.assertIs(sig.return_annotation, sig.empty)
    sig = sig.replace(return_annotation=42)
    self.assertEqual(sig.return_annotation, 42)
    self.assertEqual(sig, inspect.signature(test))
