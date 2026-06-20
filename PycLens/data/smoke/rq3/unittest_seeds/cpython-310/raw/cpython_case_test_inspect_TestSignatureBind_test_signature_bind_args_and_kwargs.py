# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_args_and_kwargs

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(a, b, c=3, **kwargs):
        return (a, b, c, kwargs)
    self.assertEqual(self.call(test, 1, 2), (1, 2, 3, {}))
    self.assertEqual(self.call(test, 1, 2, foo='bar', spam='ham'), (1, 2, 3, {'foo': 'bar', 'spam': 'ham'}))
    self.assertEqual(self.call(test, b=2, a=1, foo='bar', spam='ham'), (1, 2, 3, {'foo': 'bar', 'spam': 'ham'}))
    self.assertEqual(self.call(test, a=1, b=2, foo='bar', spam='ham'), (1, 2, 3, {'foo': 'bar', 'spam': 'ham'}))
    self.assertEqual(self.call(test, 1, b=2, foo='bar', spam='ham'), (1, 2, 3, {'foo': 'bar', 'spam': 'ham'}))
    self.assertEqual(self.call(test, 1, b=2, c=4, foo='bar', spam='ham'), (1, 2, 4, {'foo': 'bar', 'spam': 'ham'}))
    self.assertEqual(self.call(test, 1, 2, 4, foo='bar'), (1, 2, 4, {'foo': 'bar'}))
    self.assertEqual(self.call(test, c=5, a=4, b=3), (4, 3, 5, {}))
