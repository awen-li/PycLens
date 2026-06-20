# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_with_self_arg

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, self, b):
        pass
    sig = inspect.signature(test)
    ba = sig.bind(1, 2, 3)
    self.assertEqual(ba.args, (1, 2, 3))
    ba = sig.bind(1, self=2, b=3)
    self.assertEqual(ba.args, (1, 2, 3))
