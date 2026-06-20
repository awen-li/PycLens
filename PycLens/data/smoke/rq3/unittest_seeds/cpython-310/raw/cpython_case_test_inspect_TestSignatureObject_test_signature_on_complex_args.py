# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureObject_test_signature_on_complex_args

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, b: 'foo'=10, *args: 'bar', spam: 'baz', ham=123, **kwargs: int):
        pass
    self.assertEqual(self.signature(test), ((('a', ..., ..., 'positional_or_keyword'), ('b', 10, 'foo', 'positional_or_keyword'), ('args', ..., 'bar', 'var_positional'), ('spam', ..., 'baz', 'keyword_only'), ('ham', 123, ..., 'keyword_only'), ('kwargs', ..., int, 'var_keyword')), ...))
