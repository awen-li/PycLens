# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_without_self

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test_args_only(*args):
        pass

    def test_args_kwargs_only(*args, **kwargs):
        pass

    class A:

        @classmethod
        def test_classmethod(*args):
            pass

        @staticmethod
        def test_staticmethod(*args):
            pass
        f1 = functools.partialmethod(test_classmethod, 1)
        f2 = functools.partialmethod(test_args_only, 1)
        f3 = functools.partialmethod(test_staticmethod, 1)
        f4 = functools.partialmethod(test_args_kwargs_only, 1)
    self.assertEqual(self.signature(test_args_only), ((('args', ..., ..., 'var_positional'),), ...))
    self.assertEqual(self.signature(test_args_kwargs_only), ((('args', ..., ..., 'var_positional'), ('kwargs', ..., ..., 'var_keyword')), ...))
    self.assertEqual(self.signature(A.f1), ((('args', ..., ..., 'var_positional'),), ...))
    self.assertEqual(self.signature(A.f2), ((('args', ..., ..., 'var_positional'),), ...))
    self.assertEqual(self.signature(A.f3), ((('args', ..., ..., 'var_positional'),), ...))
    self.assertEqual(self.signature(A.f4), ((('args', ..., ..., 'var_positional'), ('kwargs', ..., ..., 'var_keyword')), ...))
