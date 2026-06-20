# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_partialmethod

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self
    from functools import partialmethod

    class Spam:

        def test():
            pass
        ham = partialmethod(test)
    with self.assertRaisesRegex(ValueError, 'has incorrect arguments'):
        inspect.signature(Spam.ham)

    class Spam:

        def test(it, a, *, c) -> 'spam':
            pass
        ham = partialmethod(test, c=1)
    self.assertEqual(self.signature(Spam.ham, eval_str=False), ((('it', ..., ..., 'positional_or_keyword'), ('a', ..., ..., 'positional_or_keyword'), ('c', 1, ..., 'keyword_only')), 'spam'))
    self.assertEqual(self.signature(Spam().ham, eval_str=False), ((('a', ..., ..., 'positional_or_keyword'), ('c', 1, ..., 'keyword_only')), 'spam'))

    class Spam:

        def test(self: 'anno', x):
            pass
        g = partialmethod(test, 1)
    self.assertEqual(self.signature(Spam.g, eval_str=False), ((('self', ..., 'anno', 'positional_or_keyword'),), ...))
