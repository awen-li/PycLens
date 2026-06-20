# pybcsec-seed-target: __pybcsec_seed__
# source: data/smoke/rq3/cpython_sources/cpython-3.10.12/Lib/test/test_inspect.py
# case: TestSignatureBind_test_signature_bind_kwonly

def __pybcsec_seed__():
    self = __pybcsec_self__ = object()
    __pybcsec_self__ = self

    def test(*, foo):
        return foo
    with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
        self.call(test, 1)
    self.assertEqual(self.call(test, foo=1), 1)

    def test(a, *, foo=1, bar):
        return foo
    with self.assertRaisesRegex(TypeError, "missing a required argument: 'bar'"):
        self.call(test, 1)

    def test(foo, *, bar):
        return (foo, bar)
    self.assertEqual(self.call(test, 1, bar=2), (1, 2))
    self.assertEqual(self.call(test, bar=2, foo=1), (1, 2))
    with self.assertRaisesRegex(TypeError, "got an unexpected keyword argument 'spam'"):
        self.call(test, bar=2, foo=1, spam=10)
    with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
        self.call(test, 1, 2)
    with self.assertRaisesRegex(TypeError, 'too many positional arguments'):
        self.call(test, 1, 2, bar=2)
    with self.assertRaisesRegex(TypeError, "got an unexpected keyword argument 'spam'"):
        self.call(test, 1, bar=2, spam='ham')
    with self.assertRaisesRegex(TypeError, "missing a required argument: 'bar'"):
        self.call(test, 1)

    def test(foo, *, bar, **bin):
        return (foo, bar, bin)
    self.assertEqual(self.call(test, 1, bar=2), (1, 2, {}))
    self.assertEqual(self.call(test, foo=1, bar=2), (1, 2, {}))
    self.assertEqual(self.call(test, 1, bar=2, spam='ham'), (1, 2, {'spam': 'ham'}))
    self.assertEqual(self.call(test, spam='ham', foo=1, bar=2), (1, 2, {'spam': 'ham'}))
    with self.assertRaisesRegex(TypeError, "missing a required argument: 'foo'"):
        self.call(test, spam='ham', bar=2)
    self.assertEqual(self.call(test, 1, bar=2, bin=1, spam=10), (1, 2, {'bin': 1, 'spam': 10}))
