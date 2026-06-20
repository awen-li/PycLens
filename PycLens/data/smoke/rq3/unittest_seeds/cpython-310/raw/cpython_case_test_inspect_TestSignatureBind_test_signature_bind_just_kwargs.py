# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_just_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(**kwargs):
        return kwargs
    self.assertEqual(self.call(test), {})
    self.assertEqual(self.call(test, foo='bar', spam='ham'), {'foo': 'bar', 'spam': 'ham'})
