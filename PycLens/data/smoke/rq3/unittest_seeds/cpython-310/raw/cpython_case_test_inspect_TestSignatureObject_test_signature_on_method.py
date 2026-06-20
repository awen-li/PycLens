# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_method

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    class Test:

        def __init__(*args):
            pass

        def m1(self, arg1, arg2=1) -> int:
            pass

        def m2(*args):
            pass

        def __call__(*, a):
            pass
    self.assertEqual(self.signature(Test().m1), ((('arg1', ..., ..., 'positional_or_keyword'), ('arg2', 1, ..., 'positional_or_keyword')), int))
    self.assertEqual(self.signature(Test().m2), ((('args', ..., ..., 'var_positional'),), ...))
    self.assertEqual(self.signature(Test), ((('args', ..., ..., 'var_positional'),), ...))
    with self.assertRaisesRegex(ValueError, 'invalid method signature'):
        self.signature(Test())
