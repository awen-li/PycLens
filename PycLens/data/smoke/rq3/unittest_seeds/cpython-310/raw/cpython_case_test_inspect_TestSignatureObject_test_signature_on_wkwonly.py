# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_wkwonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(*, a: float, b: str) -> int:
        pass
    self.assertEqual(self.signature(test), ((('a', ..., float, 'keyword_only'), ('b', ..., str, 'keyword_only')), int))
